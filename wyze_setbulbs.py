import os
import re
import sys
from pathlib import Path
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

if getattr(sys, "frozen", False):
    # Running as bundled exe — look for .env next to the exe
    env_path = Path(sys.executable).parent / ".env"
else:
    # Running as script — look in project folder
    env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

from wyze_sdk import Client

# Static mapping of logical bulb names to physical hardware.
# MAC addresses come from the .env file so they never live in scene data.
BULB_HARDWARE = {
    "desk_lamp": {"mac": os.getenv("DESK_LAMP_MAC"), "model": "WLPA19C"},
    "overhead_left": {"mac": os.getenv("OVERHEAD_1_MAC"), "model": "WLPA19C"},
    "overhead_right": {"mac": os.getenv("OVERHEAD_2_MAC"), "model": "WLPA19C"},
    "floor_lamp": {"mac": os.getenv("FLOOR_LAMP_MAC"), "model": "WLPA19C"},
}


def get_wyze_client():
    print("Authenticating with Wyze...")
    login_response = Client().login(
        email=os.getenv("WYZE_EMAIL"),
        password=os.getenv("WYZE_PASSWORD"),
        key_id=os.getenv("WYZE_KEY_ID"),
        api_key=os.getenv("WYZE_API_KEY"),
    )
    return Client(token=login_response["access_token"])


def validate_bulb_config(bulb_key, config):
    """Raises ValueError if a bulb's scene config has obvious problems."""
    if "color" in config:
        if not re.fullmatch(r"[0-9A-Fa-f]{6}", config["color"]):
            raise ValueError(
                f"{bulb_key}: invalid hex color '{config['color']}' (use 6-char hex, no '#')"
            )
    if "brightness" in config:
        if not (1 <= config["brightness"] <= 100):
            raise ValueError(
                f"{bulb_key}: brightness must be 1–100, got {config['brightness']}"
            )


def apply_single_bulb(client, bulb_key, scene_config):
    """Applies a single bulb's scene config using the hardware map. Returns (key, success, error)."""
    hardware = BULB_HARDWARE.get(bulb_key)
    if hardware is None:
        return (
            bulb_key,
            False,
            f"Unknown bulb key '{bulb_key}' — not in BULB_HARDWARE",
        )

    mac = hardware["mac"]
    model = hardware["model"]

    try:
        validate_bulb_config(bulb_key, scene_config)

        if not scene_config.get("is_on", True):
            client.bulbs.turn_off(device_mac=mac, device_model=model)
            return (bulb_key, True, None)

        client.bulbs.turn_on(device_mac=mac, device_model=model)

        if "color" in scene_config:
            client.bulbs.set_color(
                device_mac=mac, device_model=model, color=scene_config["color"]
            )
        elif "color_temp" in scene_config:
            client.bulbs.set_color_temp(
                device_mac=mac,
                device_model=model,
                color_temp=scene_config["color_temp"],
            )

        if "brightness" in scene_config:
            client.bulbs.set_brightness(
                device_mac=mac,
                device_model=model,
                brightness=scene_config["brightness"],
            )

        return (bulb_key, True, None)

    except Exception as e:
        return (bulb_key, False, str(e))


def apply_scene(client, bulbs: dict):
    """
    Takes a pre-authenticated Wyze client and a dict of { bulb_key: scene_config },
    and applies them in parallel. The client is created once at app startup and
    reused across all button presses to avoid re-authenticating every time.
    """
    print("Applying settings to bulbs...")

    results = []
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(apply_single_bulb, client, bulb_key, scene_config): bulb_key
            for bulb_key, scene_config in bulbs.items()
        }
        for future in as_completed(futures):
            results.append(future.result())

    succeeded = [key for key, ok, _ in results if ok]
    failed = [(key, err) for key, ok, err in results if not ok]

    for key in succeeded:
        print(f"✓ {key}")
    for key, err in failed:
        print(f"✗ {key}: {err}")

    print(f"\nDone — {len(succeeded)}/{len(bulbs)} bulbs updated successfully.")

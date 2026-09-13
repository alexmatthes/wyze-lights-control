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
from wyze_sdk.models.devices import DeviceModels

# wyze_sdk (as of 2.3.8, the latest release) doesn't yet recognize "HL_A19C2"
# (the newer color mesh bulb used in outdoor fixtures) as a mesh bulb, so its
# turn_on/set_color/set_brightness calls reject it with "not supported" even
# though it uses the same mesh-property API as WLPA19C. Register it ourselves.
if "HL_A19C2" not in DeviceModels.MESH_BULB:
    DeviceModels.MESH_BULB.append("HL_A19C2")
    DeviceModels.BULB.append("HL_A19C2")

# Static mapping of logical bulb names to physical hardware.
# MAC addresses come from the .env file so they never live in scene data.
BULB_HARDWARE = {
    "desk_lamp": {"mac": os.getenv("DESK_LAMP_MAC"), "model": "WLPA19C"},
    "overhead_left": {"mac": os.getenv("OVERHEAD_1_MAC"), "model": "WLPA19C"},
    "overhead_right": {"mac": os.getenv("OVERHEAD_2_MAC"), "model": "WLPA19C"},
    "floor_lamp": {"mac": os.getenv("FLOOR_LAMP_MAC"), "model": "WLPA19C"},
    "front_door_left": {"mac": os.getenv("FRONT_DOOR_BULB_L_MAC"), "model": "HL_A19C2"},
    "front_door_right": {"mac": os.getenv("FRONT_DOOR_BULB_R_MAC"), "model": "HL_A19C2"},
    "garage_left": {"mac": os.getenv("GARAGE_BULB_L_MAC"), "model": "HL_A19C2"},
    "garage_right": {"mac": os.getenv("GARAGE_BULB_R_MAC"), "model": "HL_A19C2"},
}

# Static mapping of logical plug names to physical hardware.
# Plugs only support on/off — no color or brightness.
# Outdoor plug outlets use model "WLPPO-SUB" and their "-000N" sub-device mac
# (not the WLPPO base station mac, which isn't individually switchable).
PLUG_HARDWARE = {
    "backyard_1": {"mac": os.getenv("BACKYARD_PLUG_1_MAC"), "model": "WLPPO-SUB"},
    "backyard_2": {"mac": os.getenv("BACKYARD_PLUG_2_MAC"), "model": "WLPPO-SUB"},
    "string_lights": {"mac": os.getenv("STRING_LIGHTS_PLUG_MAC"), "model": "WLPPO-SUB"},
    "spotlights": {"mac": os.getenv("SPOTLIGHTS_PLUG_MAC"), "model": "WLPPO-SUB"},
    "star": {"mac": os.getenv("STAR_PLUG_MAC"), "model": "WLPP1CFH"},
    "christmas_tree": {"mac": os.getenv("CHRISTMAS_TREE_PLUG_MAC"), "model": "WLPP1CFH"},
    "palm_tree": {"mac": os.getenv("PALM_TREE_PLUG_MAC"), "model": "WLPP1CFH"},
    "fan": {"mac": os.getenv("FAN_PLUG_MAC"), "model": "WLPP1CFH"},
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


def apply_single_plug(client, plug_key, scene_config):
    """Applies a single plug's scene config using the hardware map. Returns (key, success, error)."""
    hardware = PLUG_HARDWARE.get(plug_key)
    if hardware is None:
        return (
            plug_key,
            False,
            f"Unknown plug key '{plug_key}' — not in PLUG_HARDWARE",
        )

    mac = hardware["mac"]
    model = hardware["model"]

    try:
        if scene_config.get("is_on", True):
            client.plugs.turn_on(device_mac=mac, device_model=model)
        else:
            client.plugs.turn_off(device_mac=mac, device_model=model)

        return (plug_key, True, None)

    except Exception as e:
        return (plug_key, False, str(e))


def apply_scene(client, scene: dict):
    """
    Takes a pre-authenticated Wyze client and a scene dict with "bulbs" and/or
    "plugs" keys ({ device_key: scene_config }), and applies them all in
    parallel. The client is created once at app startup and reused across all
    button presses to avoid re-authenticating every time.
    """
    print("Applying scene...")

    bulbs = scene.get("bulbs", {})
    plugs = scene.get("plugs", {})

    results = []
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(apply_single_bulb, client, bulb_key, scene_config): bulb_key
            for bulb_key, scene_config in bulbs.items()
        }
        futures.update({
            executor.submit(apply_single_plug, client, plug_key, scene_config): plug_key
            for plug_key, scene_config in plugs.items()
        })
        for future in as_completed(futures):
            results.append(future.result())

    succeeded = [key for key, ok, _ in results if ok]
    failed = [(key, err) for key, ok, err in results if not ok]

    for key in succeeded:
        print(f"✓ {key}")
    for key, err in failed:
        print(f"✗ {key}: {err}")

    total = len(bulbs) + len(plugs)
    print(f"\nDone — {len(succeeded)}/{total} devices updated successfully.")

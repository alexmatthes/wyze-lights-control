import os
import re
from dotenv import load_dotenv

load_dotenv()

from wyze_sdk import Client
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_wyze_client():
    print("Authenticating with Wyze...")
    login_response = Client().login(
        email=os.getenv('WYZE_EMAIL'),
        password=os.getenv('WYZE_PASSWORD'),
        key_id=os.getenv('WYZE_KEY_ID'),
        api_key=os.getenv('WYZE_API_KEY')
    )
    return Client(token=login_response['access_token'])

def validate_bulb_config(bulb):
    """Raises ValueError if config has obvious problems."""
    if "color" in bulb:
        if not re.fullmatch(r"[0-9A-Fa-f]{6}", bulb["color"]):
            raise ValueError(f"{bulb['name']}: invalid hex color '{bulb['color']}' (use 6-char hex, no '#')")
    if "brightness" in bulb:
        if not (1 <= bulb["brightness"] <= 100):
            raise ValueError(f"{bulb['name']}: brightness must be 1–100, got {bulb['brightness']}")

def apply_single_bulb(client, bulb):
    """Applies config to one bulb. Returns (name, success, error)."""
    mac, model, name = bulb['mac'], bulb['model'], bulb['name']
    try:
        validate_bulb_config(bulb)
        if not bulb.get("is_on", True):
            client.bulbs.turn_off(device_mac=mac, device_model=model)
            return (name, True, None)

        client.bulbs.turn_on(device_mac=mac, device_model=model)
        if "color" in bulb:
            client.bulbs.set_color(device_mac=mac, device_model=model, color=bulb['color'])
        elif "color_temp" in bulb:
            client.bulbs.set_color_temp(device_mac=mac, device_model=model, color_temp=bulb['color_temp'])
        if "brightness" in bulb:
            client.bulbs.set_brightness(device_mac=mac, device_model=model, brightness=bulb['brightness'])
        return (name, True, None)
    except Exception as e:
        return (name, False, str(e))

def apply_scene(bulbs_config):
    """Takes a list of bulb configurations and applies them in parallel."""
    client = get_wyze_client()
    print("Applying settings to bulbs...")

    results = []
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(apply_single_bulb, client, bulb): bulb for bulb in bulbs_config}
        for future in as_completed(futures):
            results.append(future.result())

    succeeded = [name for name, ok, _ in results if ok]
    failed = [(name, err) for name, ok, err in results if not ok]

    for name in succeeded:
        print(f"✓ {name}")
    for name, err in failed:
        print(f"✗ {name}: {err}")

    print(f"\nDone — {len(succeeded)}/{len(bulbs_config)} bulbs updated successfully.")

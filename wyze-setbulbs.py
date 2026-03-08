import os
from dotenv import load_dotenv
from wyze_sdk import Client

def get_wyze_client():
    """Loads secrets and authenticates with Wyze."""
    load_dotenv()
    print("Authenticating with Wyze...")
    login_response = Client().login(
        email=os.getenv('WYZE_EMAIL'),
        password=os.getenv('WYZE_PASSWORD'),
        key_id=os.getenv('WYZE_KEY_ID'),
        api_key=os.getenv('WYZE_API_KEY')
    )
    return Client(token=login_response['access_token'])

def apply_scene(bulbs_config):
    """Takes a list of bulb configurations and applies them."""
    client = get_wyze_client()
    print("Applying settings to bulbs...")

    for bulb in bulbs_config:
        mac = bulb['mac']
        model = bulb['model']
        name = bulb['name']

        try:
            # Check if the bulb should be explicitly turned off
            if not bulb.get("is_on", True):
                client.bulbs.turn_off(device_mac=mac, device_model=model)
                print(f"Turned off {name}")
                continue  # Skip the rest of the loop for this bulb

            # Otherwise, turn the bulb on
            client.bulbs.turn_on(device_mac=mac, device_model=model)

            # Apply either a hex color or a color temperature
            if "color" in bulb:
                client.bulbs.set_color(device_mac=mac, device_model=model, color=bulb['color'])
            elif "color_temp" in bulb:
                client.bulbs.set_color_temp(device_mac=mac, device_model=model, color_temp=bulb['color_temp'])

            # Apply brightness if specified
            if "brightness" in bulb:
                client.bulbs.set_brightness(device_mac=mac, device_model=model, brightness=bulb['brightness'])

            print(f"Successfully updated {name}")

        except Exception as e:
            print(f"Failed to update {name}: {e}")

    print("All done!")

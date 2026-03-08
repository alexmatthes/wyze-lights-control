import os
from dotenv import load_dotenv
from wyze_sdk import Client

# 1. Load the secrets from the .env file
load_dotenv()

# 2. Log in and get the access token using the environment variables
print("Authenticating with Wyze...")
login_response = Client().login(
    email=os.getenv('WYZE_EMAIL'),
    password=os.getenv('WYZE_PASSWORD'),
    key_id=os.getenv('WYZE_KEY_ID'),
    api_key=os.getenv('WYZE_API_KEY')
)

# 3. Create the client using the temporary token
client = Client(token=login_response['access_token'])

# 4. Define your bulb settings here
bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 5000,
        "brightness": 100
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Keep the ceiling dark
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Keep the ceiling dark
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 5000,
        "brightness": 80
    }
]

# 5. Loop through the configuration and apply the settings
print("Applying settings to bulbs...")
for bulb in bulbs_config:
    try:
        # Check if the bulb should be off
        if not bulb.get("is_on", True):
            client.bulbs.turn_off(device_mac=bulb['mac'], device_model=bulb['model']) #
            print(f"Turned off {bulb['name']}")

        # Otherwise, turn it on and set the colors
        else:
            client.bulbs.turn_on(device_mac=bulb['mac'], device_model=bulb['model']) #
            if "color" in bulb:
              client.bulbs.set_color(device_mac=bulb['mac'], device_model=bulb['model'], color=bulb['color'])
            elif "color_temp" in bulb:
              client.bulbs.set_color_temp(device_mac=bulb['mac'], device_model=bulb['model'], color_temp=bulb['color_temp'])
            client.bulbs.set_brightness(device_mac=bulb['mac'], device_model=bulb['model'], brightness=bulb['brightness']) #
            print(f"Successfully updated {bulb['name']}")

    except Exception as e:
        print(f"Failed to update {bulb['name']}: {e}")

print("All done!")

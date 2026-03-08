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
# Brightness is an integer from 1 to 100. Color is a standard Hex string.
bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "color": "00FFFF",       # Cyan - A cool, bright accent near your screen
        "brightness": 35         # Kept moderate to avoid screen glare
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "color": "FF4500",       # Deep Indigo - Very dark blue/purple
        "brightness": 10         # Very dim for that moody overhead atmosphere
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "color": "FF4500",       # Dark Violet - Slightly warmer deep purple
        "brightness": 10         # Very dim to match the other overhead
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "color": "0000FF",       # Rose/Magenta - A warm, vibrant wash of color
        "brightness": 45         # Bright enough to light the corner of the room softly
    }
]

# 5. Loop through the configuration and apply the settings
print("Applying settings to bulbs...")
for bulb in bulbs_config:
    try:
        # Set the color
        client.bulbs.set_color(
            device_mac=bulb['mac'],
            device_model=bulb['model'],
            color=bulb['color']
        )

        # Set the brightness
        client.bulbs.set_brightness(
            device_mac=bulb['mac'],
            device_model=bulb['model'],
            brightness=bulb['brightness']
        )

        print(f"Successfully updated {bulb['name']}")
    except Exception as e:
        print(f"Failed to update {bulb['name']}: {e}")

print("All done!")

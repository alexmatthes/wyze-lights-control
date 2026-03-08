import os
from wyze-setbulbs import apply_scene

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF8C00",       # Dark Gold / Amber - luxurious and warm
        "brightness": 25         # Low enough to cast a soft glow
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
        "color": "FF3300",       # Deep Orange-Red - adds a warm, fiery depth to the room
        "brightness": 20         # Kept very dim to let the gold stand out
    }
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

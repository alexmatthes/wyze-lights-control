import os
from wyze_setbulbs import apply_scene

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "color": "00FFFF",       # Cyan - A cool, bright accent near your screen
        "brightness": 50         # Kept moderate to avoid screen glare
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "color": "330066",       # Deep Indigo - Very dark blue/purple
        "brightness": 15         # Very dim for that moody overhead atmosphere
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "color": "4B0082",       # Dark Violet - Slightly warmer deep purple
        "brightness": 15         # Very dim to match the other overhead
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "color": "FF007F",       # Rose/Magenta - A warm, vibrant wash of color
        "brightness": 40         # Bright enough to light the corner of the room softly
    }
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

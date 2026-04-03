import os
from wyze_setbulbs import apply_scene

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FFD700",       # Gold - mimics a torch glow right at your desk
        "brightness": 35         # Warm but not bright, like a single torch nearby
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Cave ceiling stays dark
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Cave ceiling stays dark
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "1A6B1A",       # Deep Mossy Green - like cave moss or a distant Nether portal shimmer
        "brightness": 18         # Barely there, just enough to give the room an eerie depth
    }
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

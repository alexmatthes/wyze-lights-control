import os
from wyze_setbulbs import apply_scene

# SCENE: Movie Night
#
# Lighting philosophy: replicate the feel of a real cinema.
#
# The overheads are cut completely — they'd wash out the screen and kill
# contrast. The desk lamp (near your screen) gets a deep amber bias light
# at very low intensity; this is a classic cinematographer's trick that
# reduces eye strain by softening the harsh contrast between a bright
# display and a pitch-black room. The floor lamp becomes your "aisle
# light" — warm, extremely dim, just enough to navigate safely without
# pulling your eyes away from the screen.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF4500",       # Deep amber-orange - classic bias lighting behind/beside the screen
        "brightness": 12         # Barely there — just enough to soften the screen-to-dark contrast
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Off entirely — overheads create glare and kill immersion
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Off entirely — matches overhead left
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF2200",       # Deep red - preserves night vision, won't reflect on the screen
        "brightness": 8          # Barely visible — think 'exit sign', not 'reading lamp'
    }
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

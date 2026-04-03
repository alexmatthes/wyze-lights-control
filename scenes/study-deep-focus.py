import os
from wyze_setbulbs import apply_scene

# SCENE: Study / Deep Focus
#
# Lighting philosophy: a single, clean key light with neutral fill.
#
# Stage lighting for drama uses high contrast; lighting for precision work —
# surgical theaters, broadcast desks, drafting rooms — uses the opposite:
# controlled, even, neutral-white illumination with no color casts to mislead
# the eye or fatigue the brain. The desk lamp is your hero source: full
# brightness, pure neutral white (4000K "cool white" sits in the sweet spot
# between alerting and comfortable). The overheads provide soft fill to
# eliminate harsh shadows, but at reduced brightness so the desk lamp
# remains clearly dominant — your eye always knows where to look.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 4000,      # Neutral cool-white — alert and accurate, no color distortion
        "brightness": 100        # Full brightness — this is your primary work light
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 4000,      # Matches the desk lamp to keep the room chromatically consistent
        "brightness": 55         # Half power — ambient fill, not a competing source
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 4000,      # Matches overhead left
        "brightness": 55         # Balanced fill across the ceiling
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Off — a low source competes with the desk lamp and creates visual noise
    }
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

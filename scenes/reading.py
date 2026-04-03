import os
from wyze_setbulbs import apply_scene

# SCENE: Reading
#
# Lighting philosophy: a single warm key with soft surround fill — the
# well-designed reading nook.
#
# Reading fatigue comes from two sources: insufficient light at the page
# (forcing your pupils to dilate and strain), and excessive contrast between
# the lit page and a dark surround (causing constant re-adaptation). The fix
# is a bright, warm-white desk lamp as your hero source, paired with a very
# gentle warm fill from the floor lamp to soften the room contrast without
# competing for attention. 2700-3000K is the sweet spot: warm enough to be
# easy on the eyes over hours, cool enough to keep you alert and on the page.
# Overheads stay off — they create glare on pages and flatten the cozy,
# directional quality that makes a reading light feel like a reading light.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 2900,  # Warm white — easy on the eyes for long sessions
        "brightness": 100,  # Full brightness — you need genuine light on the page
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": False,  # Off — creates glare on pages and competes with the desk lamp
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv("OVERHEAD_2_MAC"),
        "model": "WLPA19C",
        "is_on": False,  # Off — matches overhead left
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv("FLOOR_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 2700,  # Slightly warmer than the desk lamp — recedes into the background
        "brightness": 25,  # Very soft fill — reduces room contrast without drawing the eye
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

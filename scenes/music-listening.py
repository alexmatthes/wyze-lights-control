import os
from wyze_setbulbs import apply_scene

# SCENE: Music Listening Session
#
# Lighting philosophy: the aesthetic of a small, intimate live venue.
#
# Think a jazz club, a small theater black box, or a vinyl listening bar.
# The overheads are off — venues don't light audiences from above. Instead,
# a warm amber "stage wash" from the floor lamp evokes footlights and
# practicals, while the desk lamp becomes a single focused "special" in
# deep gold — the kind of isolated pool of light that makes a room feel
# curated and intentional. The overall effect is warm, focused, and
# immersive: a room that feels like it was dressed for listening.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FFB300",  # Deep gold — warm key light, like a tungsten fresnel
        "brightness": 45,  # Moderate — a pool of light, not a floodlight
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": False,  # Off — overhead sources flatten a room's sense of intimacy
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
        "color": "FF5500",  # Burnt orange — a warm, low wash like practical stage lighting
        "brightness": 55,  # The dominant source in the room; sets the overall mood
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

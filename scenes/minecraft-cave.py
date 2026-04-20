import os
from wyze_setbulbs import apply_scene

# SCENE: Minecraft Cave
#
# Lighting philosophy: torch-and-moss spelunking, rendered in real light.
#
# A Minecraft cave is lit by exactly two things: a torch (warm, close,
# yellow-gold), and whatever ambient phenomena drift in — lava's amber
# flicker, glowing moss, a distant Nether-portal shimmer. This scene maps
# one-to-one. The desk lamp is the torch held out in front of you: a
# close, warm gold with a practical's reach of about three feet. The floor
# lamp becomes the cave's ambient phenomenon — a barely-there mossy green
# uplight that suggests something glowing in the corners without ever
# quite showing it. The overheads stay solid black: above the torch,
# there is only stone.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FFB000",  # Torch gold — warm, slightly orange-biased, close-range
        "brightness": 38,   # One torch-arm of reach; a practical, not a room light
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": False,   # Off — the cave ceiling is unreachable dark
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv("OVERHEAD_2_MAC"),
        "model": "WLPA19C",
        "is_on": False,   # Off — matches overhead left
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv("FLOOR_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "0F6020",  # Mossy green — a hint of glowlichen or distant cave life
        "brightness": 15,   # Barely visible; a color suggestion, not illumination
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

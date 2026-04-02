import os
from wyze_setbulbs import apply_scene

# SCENE: Lofi / Chill Hang
#
# Lighting philosophy: the golden hour that never ends.
#
# The lofi aesthetic — that sense of comfortable, slightly nostalgic ease —
# maps directly to a specific lighting condition: late afternoon sun filtered
# through a window, around 2200-2500K, casting long soft shadows. On stage
# this is called "practicals and pools": visible, warm light sources that
# feel organic rather than designed. The floor lamp becomes the dominant
# ambient glow, a soft amber wash that fills the room from below like
# last light through curtains. The desk lamp burns a dim, hazy apricot —
# present but not demanding. Overheads off. The room should feel like
# somewhere you'd stay for hours without noticing the time passing.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF7A00",       # Warm apricot — soft, hazy, like afternoon light through a shade
        "brightness": 28         # Low — a glow rather than a light source
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Off — overheads kill the intimate, low-light chill atmosphere
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "is_on": False           # Off — matches overhead left
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF4500",       # Deep amber — the soul of the scene, warm and enveloping
        "brightness": 50         # The room's heartbeat; present, but never harsh
    }
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

import os
from wyze_setbulbs import apply_scene

# SCENE: Party / Hype Mode
#
# Lighting philosophy: nightclub color contrast — split complementaries at war.
#
# High-energy club and concert lighting works by creating tension: opposing
# colors on the spectrum fight each other visually, producing a sense of
# electric, unstable energy that reads as excitement. Here, the overheads
# go head-to-head — one deep magenta, one electric blue — a classic
# split-complementary clash. The floor lamp anchors in hot acid green,
# the most visually aggressive color on the spectrum. The desk lamp punches
# in vivid violet to bridge the blue and magenta. Everything at high
# brightness, no apologies.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "8B00FF",  # Vivid violet — bridges the blue/magenta clash on the ceiling
        "brightness": 90,  # Bright and punchy near eye level
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF0080",  # Hot magenta — aggressive, high-energy pink
        "brightness": 100,  # Full power for maximum color saturation on the walls
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv("OVERHEAD_2_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "0033FF",  # Electric blue — direct opponent to the magenta overhead
        "brightness": 100,  # Matched full power to keep the clash even
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv("FLOOR_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "39FF14",  # Acid green — neon, abrasive, and maximally energizing
        "brightness": 85,  # Very bright low source; bounces up the walls dramatically
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

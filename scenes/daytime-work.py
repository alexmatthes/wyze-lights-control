import os
from wyze_setbulbs import apply_scene

# SCENE: Daytime Work / Neutral
#
# Lighting philosophy: horizon-daylight balance — the modern office, done well.
#
# 5000K sits at the color temperature of direct sun a few hours after
# sunrise — cool enough to promote alertness and accurate color perception,
# warm enough to avoid the clinical, blue-cast feel of 6500K that fatigues
# many people over long sessions. It's the white point broadcast studios
# and graphic-design monitors target as their working default, precisely
# because it's the color of "neutral daylight" to the human eye. The desk
# lamp anchors the scene at full power; the floor lamp provides matched-
# temperature fill that lifts the lower half of the room without shifting
# the palette. Overheads stay off to preserve a clear directional quality
# — a desk you sit AT, not just a room you occupy.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 5000,  # Horizon daylight — alert and color-accurate without the clinical edge
        "brightness": 100,   # Full power; hero source on the work surface
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": False,   # Off — preserves the desk's directional quality
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
        "color_temp": 5000,  # Matched to the desk lamp — consistent white point across the room
        "brightness": 80,    # Strong fill; lifts shadow without overpowering the desk
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

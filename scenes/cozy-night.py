import os
from wyze_setbulbs import apply_scene

# SCENE: Cozy Night
#
# Lighting philosophy: the hearth, relocated to a bedroom.
#
# "Cozy" as a lighting state is defined almost entirely by low, warm sources:
# hearths, candles, a single lamp on a side table. High-angle light reads
# as "daylight" or "office" and kills the feeling instantly — so the overheads
# go fully dark. The floor lamp takes the role of the hearth itself, an
# ember-red uplight below eye level, as if something were burning low in
# the corner. The desk lamp becomes the "candle on the table" — a small,
# warm gold source at forearm distance. Together they produce the
# unmistakable impression of a room that has been warmed, not lit.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF9A30",  # Warm amber gold — ~2100K in feel, candle-adjacent
        "brightness": 22,   # Dim and close; the tabletop candle, never a task light
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": False,   # Off — any overhead light breaks the hearth illusion
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
        "color": "FF3000",  # Ember red — the fireplace in the corner, warm uplight wash
        "brightness": 20,   # A glow, never a flame; the room's heartbeat
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

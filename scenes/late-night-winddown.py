import os
from wyze_setbulbs import apply_scene

# SCENE: Late Night Wind-Down
#
# Lighting philosophy: trick your brain into thinking it's dusk.
#
# Blue light suppresses melatonin production — it signals "daytime" to your
# circadian rhythm and delays sleep. This scene strips out all blue entirely,
# using only the deepest warm amber tones at very low brightness. The effect
# is candlelight-adjacent: ancient, calming, and physiologically sleep-friendly.
# Only the floor lamp is on to keep light sources low in the room (high sources
# read as "sun", low sources read as "fire" — your brain knows the difference).

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": False,  # Off — too close to your eyes at a desk level
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": False,  # Off — overhead light is the worst offender for melatonin suppression
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
        "color": "FF2800",  # Deep ember red — essentially zero blue content
        "brightness": 18,  # Dim enough to be soothing, bright enough to move around safely
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

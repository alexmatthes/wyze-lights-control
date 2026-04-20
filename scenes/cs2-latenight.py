import os
from wyze_setbulbs import apply_scene

# SCENE: CS2 / Late-Night Competitive
#
# Lighting philosophy: the LAN-center look — cold, quiet, forward-focused.
#
# Competitive play at 1 AM asks for sharpened attention without the
# circadian hit of bright cool-white light. The answer is cool chroma
# instead of cool color temperature: a deep, saturated blue palette at
# low brightness reads as "alert" to the eye without flooding the retina
# with the melatonin-suppressing daylight white that would wreck sleep
# an hour later. A pale cyan bias behind the screen reduces contrast
# fatigue during long rounds. The overheads drop to a near-black icy
# navy — stadium-style peripheral color, not illumination. The floor
# lamp anchors the "pit" in cobalt, a single saturated low source that
# pulls the room's focus forward onto the monitor.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "80E8FF",  # Pale cyan — bias light tuned to a cool monitor white point
        "brightness": 28,   # Bias-level; any higher and it reflects onto the screen
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "001A66",  # Icy navy — a ceiling color, not a light source
        "brightness": 8,    # Near-black; peripheral color only
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv("OVERHEAD_2_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "001A66",  # Matched to overhead left for balanced ceiling coverage
        "brightness": 8,
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv("FLOOR_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "0033FF",  # Cobalt — the saturated anchor; uplights the rear wall
        "brightness": 35,   # Moderate; builds the pit effect without pulling the eye back
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

import os
from wyze_setbulbs import apply_scene

# SCENE: Morning Wake-Up / Energize
#
# Lighting philosophy: simulate a bright, clear morning sky.
#
# This is the polar opposite of wind-down. High-intensity, cool-white light
# (5500-6500K) signals "noon sun" to your circadian rhythm, rapidly suppressing
# residual melatonin and boosting cortisol and alertness. Theater follow-spot
# operators know that cool, bright sources command attention — this is that
# principle applied to getting out of bed. Everything on, everything bright,
# the desk lamp gets a crisp daylight white to simulate the color temperature
# of open sky. You'll feel it within minutes.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 6500,  # Crisp daylight — the brightest, most alerting color temperature
        "brightness": 100,  # Full power — no easing in, commit to the morning
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 5500,  # Slightly softer daylight — fills the room evenly
        "brightness": 100,  # Full flood, no shadows to hide in
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv("OVERHEAD_2_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 5500,  # Matches overhead left for balanced, shadowless coverage
        "brightness": 100,
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv("FLOOR_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 5000,  # Warm-daylight fill — lifts the lower half of the room
        "brightness": 90,  # Slightly pulled back so the overheads remain dominant
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

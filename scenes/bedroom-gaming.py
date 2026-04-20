import os
from wyze_setbulbs import apply_scene

# SCENE: Bedroom Gaming / Ambient
#
# Lighting philosophy: bias-light the screen, recess the room.
#
# A cool cyan source next to the monitor acts as bias lighting: by giving
# the pupil a dim, screen-adjacent reference, it reduces the contrast
# struggle between a bright display and a dark room and cuts eye strain
# over long sessions. The overheads drop to a deep indigo whisper —
# present enough to give the ceiling depth, quiet enough to stay out of
# peripheral vision where motion would distract. The floor lamp anchors
# the room with a single magenta accent, the lone warm note in an
# otherwise cool palette; designers call this the "kicker" — one color
# that prevents a monochromatic scene from feeling sterile.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "00E0FF",  # Daylight cyan — bias light tuned near a monitor's 6500K white point
        "brightness": 30,   # Bias-level, not task-level; higher will reflect onto the screen
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "2A0060",  # Deep indigo — a color presence, not a light source
        "brightness": 12,   # Barely there; defines the ceiling without illuminating it
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv("OVERHEAD_2_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "2A0060",  # Matched to overhead left for balanced, even ceiling coverage
        "brightness": 12,
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv("FLOOR_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF1A80",  # Hot magenta — the warm kicker that keeps the cool palette alive
        "brightness": 40,   # Accent-level; visible, but subordinate to the monitor
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

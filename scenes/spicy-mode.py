import os
from wyze_setbulbs import apply_scene

# SCENE: Sensual Love Mode / Spicy
#
# Lighting philosophy: skin-on-skin closeness — warm, blood-rush tones that flatter every curve
# and make pupils dilate. Deep rose-red and burgundy bathe the room in intimate heat,
# while a soft amber/gold glow mimics candlelight or flushed skin. Overheads stay off or
# extremely subdued so shadows caress rather than expose. Everything dim, slow, inviting —
# the visual equivalent of a low whisper and lingering touch.

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv('DESK_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "B22222",       # Firebrick / deep warm red — blood-rush, kiss-flushed intimacy
        "brightness": 35         # Moderate glow — close enough to feel personal and heated
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv('OVERHEAD_1_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "4B0082",       # Deep indigo-violet — mysterious, seductive shadow layer
        "brightness": 12         # Barely there — just enough to give the ceiling a sultry bruise
    },
    {
        "name": "Overhead Right",
        "mac": os.getenv('OVERHEAD_2_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "800020",       # Burgundy / oxblood — rich, luxurious, carnal depth
        "brightness": 12         # Matches the other overhead; creates subtle color tension
    },
    {
        "name": "Floor Lamp",
        "mac": os.getenv('FLOOR_LAMP_MAC'),
        "model": "WLPA19C",
        "is_on": True,
        "color": "FF8C00",       # Dark amber / torch-like — warmest, most skin-flattering tone
        "brightness": 28         # Low but golden — spills soft light upward like candle flicker
    }
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

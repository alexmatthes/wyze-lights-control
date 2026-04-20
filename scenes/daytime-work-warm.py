import os
from wyze_setbulbs import apply_scene

# SCENE: Daytime Work / Warm
#
# Lighting philosophy: afternoon office, not morning office.
#
# 2700K is the color temperature of the classic tungsten desk lamp — the
# American office standard before fluorescents took over. As a work scene
# it serves two purposes. First, for late-afternoon and evening sessions,
# the warm bias dramatically reduces blue-light exposure in the hours before
# sleep, protecting circadian rhythm. Second, for creative work: color-
# temperature studies consistently show warmer light lowers arousal and
# opens divergent thinking, while cool light favors convergent, analytical
# tasks. The desk lamp is the hero at full power; the floor lamp provides
# matched-temperature fill so the ceiling's darkness doesn't create a
# contrast cliff. Overheads stay off — warm overhead light reads as
# "hotel lobby," not "workspace."

bulbs_config = [
    {
        "name": "Desk Lamp",
        "mac": os.getenv("DESK_LAMP_MAC"),
        "model": "WLPA19C",
        "is_on": True,
        "color_temp": 2700,  # Tungsten-warm — classic desk-lamp white
        "brightness": 100,   # Full power; the hero source for the work surface
    },
    {
        "name": "Overhead Left",
        "mac": os.getenv("OVERHEAD_1_MAC"),
        "model": "WLPA19C",
        "is_on": False,   # Off — warm overheads flatten the directional quality of the desk
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
        "color_temp": 2700,  # Matched to the desk lamp — unified warm white point
        "brightness": 80,    # Strong fill to soften the dark ceiling without competing
    },
]

if __name__ == "__main__":
    apply_scene(bulbs_config)

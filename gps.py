import random


cities = [
        ("Redruth", (50.23, -5.24)),
        ("Edinburgh", (55.94, -3.27)),
        ("London", (51.52, -0.24)),
        ("Truro", (50.26, -5.08)),
        ("Vladivostok", (43.16, 131.8))
]

def get_location():
    # Dummy function, emulates a GPS
    pos = random.randint(0, len(cities)-1)
    return cities[pos][1]

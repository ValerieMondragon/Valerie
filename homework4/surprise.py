# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?
def print_star_names(target_dict):
    for name in target_dict:
        print(name)

def print_star_and_spectral_type(target_dict):
    for name, info in target_dict.items():
        spectral_type = info["Spectral Type"]
        print(f"{name}: {spectral_type}")
def stars_with_mag_greater_than_0_1(target_dict):
    print("Stars with magnitude > 0.1:")
    for name, info in target_dict.items():
        if info["Magnitude"] > 0.1:
            print(f"{name}: {info['Magnitude']}")
def dec_to_degrees(dec_str):
    """
    Convert a declination string like '+38° 47′ 01″' to decimal degrees.
    This is a simple parser tailored to the format in this file.
    """
    # Replace Unicode characters with simple ones
    dec_str = dec_str.replace("°", " ").replace("′", " ").replace("″", " ")
    parts = dec_str.split()

    sign = 1
    if parts[0].startswith("-") or parts[0].startswith("−"):
        sign = -1

    # Remove + / - sign to get numbers
    deg = float(parts[0].replace("+", "").replace("-", "").replace("−", ""))
    minutes = float(parts[1])
    seconds = float(parts[2])

    decimal = sign * (deg + minutes / 60 + seconds / 3600)
    return decimal
def brightest_star_near_dec_20(target_dict):
    """
    Find the brightest star (smallest magnitude) among those
    whose declination is closest to +20 degrees.
    """
    closest_stars = []
    min_dec_diff = None

    # First, find the smallest |Dec - 20|
    for name, info in target_dict.items():
        dec_deg = dec_to_degrees(info["Dec"])
        diff = abs(dec_deg - 20.0)

        if (min_dec_diff is None) or (diff < min_dec_diff):
            min_dec_diff = diff
            closest_stars = [(name, info)]
        elif diff == min_dec_diff:
            closest_stars.append((name, info))

    # Among the closest in declination, pick the brightest (smallest magnitude)
    brightest_name = None
    brightest_info = None
    min_mag = None

    for name, info in closest_stars:
        mag = info["Magnitude"]
        if (min_mag is None) or (mag < min_mag):
            min_mag = mag
            brightest_name = name
            brightest_info = info

    return brightest_name, brightest_info
favorite_constellation = "Orion"

if __name__ == "__main__":
    print("1) Star names:")
    print_star_names(targets)
    print()

    print("2) Star names with spectral types:")
    print_star_and_spectral_type(targets)
    print()

    print("3) Stars with magnitude > 0.1:")
    stars_with_mag_greater_than_0_1(targets)
    print()

    print("5) Brightest star whose Dec is closest to 20°:")
    name, info = brightest_star_near_dec_20(targets)
    print(f"{name}: Dec = {info['Dec']}, Magnitude = {info['Magnitude']}")
    print()

    print("6) My favorite constellation is:", favorite_constellation)


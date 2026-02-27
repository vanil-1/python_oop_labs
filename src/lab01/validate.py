import re


def normalize(string: str, casefold: bool = True, yo2e: bool = True):
    string = re.sub(r"[\x00-\x1F\x7F\u200B\uFEFF]", " ", string).casefold()
    string = " ".join(string.split())
    return string.casefold().replace("ё", "е").strip()


def validate_address(address: str):
    address = normalize(address)
    address_pattern = re.compile(r"^\d+\s[a-z]+(?:\s[a-z]+)?")
    try:
        if not address_pattern.fullmatch(address):
            raise ValueError(
                "Address must be format: <number of house street> apt. <number>!"
            )
        return address
    except TypeError:
        raise TypeError("Address must be string!")


def validate_floors(floors: int):
    if type(floors) != int:
        raise TypeError("Floors must be int!")
    elif not (0 < floors < 4):
        raise ValueError("Floors must be between 0 and 4!")
    else:
        return floors


def validate_area(area: float | int):
    try:
        if not (area > 10):
            raise ValueError("Area must be more then 10!")
        return area
    except TypeError:
        raise TypeError("Area must be float or int!")


def validate_cost(cost: float | int):
    try:
        if not (cost > 100):
            raise ValueError("Cost must be more then 100!")
        return cost
    except TypeError:
        raise TypeError("Cost must be float or int!")


def validate_min_time_rent(min_time_rent: int):
    if type(min_time_rent) != int:
        raise TypeError("Minimal time of rent must be int!")
    elif min_time_rent < 1:
        raise ValueError("Minimal time of rent must be more then 1!")
    else:
        return min_time_rent


def validate_rented(rented: bool):
    if type(rented) == bool:
        return rented
    else:
        raise TypeError("Rented must be bool!")
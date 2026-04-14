import re


def normalize(string: str):
    string = re.sub(r"[\x00-\x1F\x7F\u200B\uFEFF]", " ", string)
    string = " ".join(string.split())
    return string.casefold().strip()


def validate_address(address: str):
    if not isinstance(address, str):
        raise TypeError("Address must be string!")

    address = normalize(address)

    address_pattern = re.compile(r"^\d+\s[a-z]+(?:\s[a-z]+)?")
    if not address_pattern.fullmatch(address):
        raise ValueError(
            "Address must be format: <number of house street> apt. <number>!"
        )
    return address


def validate_floors(floors: int):
    if not isinstance(floors, int):
        raise TypeError("Floors must be int!")

    if not (0 < floors < 4):
        raise ValueError("Floors must be between 0 and 4!")

    return floors


def validate_area(area: float | int):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be float or int!")

    if area <= 10:
        raise ValueError("Area must be more then 10!")

    return area


def validate_cost(cost: float | int):
    if not isinstance(cost, (int, float)):
        raise TypeError("Cost must be float or int!")

    if cost <= 100:
        raise ValueError("Cost must be more then 100!")

    return cost


def validate_min_time_rent(min_time_rent: int):
    if not isinstance(min_time_rent, int):
        raise TypeError("Minimal time of rent must be int!")

    if min_time_rent < 1:
        raise ValueError("Minimal time of rent must be more then 1!")

    return min_time_rent


def validate_rented(rented: bool):
    if not isinstance(rented, bool):
        raise TypeError("Rented must be bool!")

    return rented


def validate_type(obj, t):
    if not isinstance(obj, t):
        raise TypeError(f"Object's type is not {t}!")


VALIDATORS = {
    "address": validate_address,
    "floors": validate_floors,
    "area": validate_area,
    "cost": validate_cost,
    "min_time_rent": validate_min_time_rent,
    "rented": validate_rented,
}

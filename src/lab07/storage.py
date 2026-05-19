import json
from typing import Any

from src.libs.models.base_house import House
from src.libs.models.private_house import PrivateHouse
from src.libs.models.commercial_house import CommercialHouse
from src.libs.models.models_map import CLASS_MAP
from src.lab07.exceptions import StorageError


def house_to_dict(house: House) -> dict[str, Any]:
    base_data = {
        "address": house.address,
        "floors": house.floors,
        "area": house.area,
        "cost": house.cost,
        "min_time_rent": house.min_time_rent,
        "rented": house.rented,
    }

    if isinstance(house, PrivateHouse):
        base_data.update(
            {
                "type": "private",
                "land_area": house.land_area,
                "heating_type": house.heating_type,
                "occupants_count": house.occupants_count,
            }
        )

    elif isinstance(house, CommercialHouse):
        base_data.update(
            {
                "type": "commercial",
                "usage_type": house.usage_type,
                "operational_area": house.operational_area,
                "customers_average_count": house.customers_average_count,
            }
        )

    else:
        raise StorageError("serialize", "unknown house type")

    return base_data


def dict_to_house(data: dict[str, Any]) -> House:
    house_type = data.get("type")

    if house_type not in CLASS_MAP:
        raise StorageError("deserialize", f"invalid type: {house_type}")

    cls = CLASS_MAP[house_type]

    base_kwargs = {
        "address": data["address"],
        "floors": data["floors"],
        "area": data["area"],
        "cost": data["cost"],
        "min_time_rent": data["min_time_rent"],
        "rented": data["rented"],
    }

    if house_type == "private":
        return cls(
            **base_kwargs,
            land_area=data["land_area"],
            heating_type=data["heating_type"],
            occupants_count=data["occupants_count"],
        )

    elif house_type == "commercial":
        return cls(
            **base_kwargs,
            usage_type=data["usage_type"],
            operational_area=data["operational_area"],
            customers_average_count=data["customers_average_count"],
        )

    raise StorageError("deserialize", "unsupported type")


def save(data: list[dict[str, Any]], filepath: str) -> None:
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except Exception as error:
        raise StorageError("save", filepath) from error


def load(filepath: str) -> list[dict[str, Any]]:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as error:
        raise StorageError("load", filepath) from error

    except Exception as error:
        raise StorageError("load", filepath) from error

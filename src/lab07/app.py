from __future__ import annotations
from typing import Any, Callable

from src.libs.collections.base_district import HousesDistrict
from src.libs.models.base_house import House
from src.libs.strategies.sortings import (
    by_address,
    by_cost,
    by_area,
    by_floors,
)
from src.libs.strategies.factories import (
    make_area_filter,
    make_cost_filter,
)
from src.libs.strategies.filters import is_not_rented

from src.lab07.exceptions import (
    HouseNotFoundError,
    StorageError,
)

from src.lab07.storage import (
    load,
    save,
    dict_to_house,
    house_to_dict,
)


class HouseApp:
    def __init__(self, district_name: str, storage_path: str) -> None:
        self._district = HousesDistrict(district_name)
        self._storage_path = storage_path

    def _get_house_by_address(self, address: str) -> House | None:
        houses = self._district.find_by("address", address)
        return houses[0] if houses else None

    def add_house(self, house: House) -> None:
        self._district.add(house)

    def remove_house(self, address: str) -> None:
        house = self._get_house_by_address(address)
        if not house:
            raise HouseNotFoundError(address)

        self._district.remove(house)

    def get_all_houses(self) -> list[House]:
        return self._district.get_all()

    def find_houses(self, field: str, value: Any) -> list[House]:
        result = self._district.find_by(field, value)
        if not result:
            raise HouseNotFoundError(str(value))

        return result

    def filter_houses(
        self, number_filter: int, value_filter: float | int
    ) -> HousesDistrict:
        mapping = {
            "1": is_not_rented,
            "2": make_cost_filter(value_filter),
            "3": make_area_filter(value_filter),
        }
        return self._district.filter_by(mapping[number_filter])

    def sort_houses(
        self, key: Callable[[House], Any], reverse: bool = False
    ) -> HousesDistrict:
        mapping = {
            "address": by_address,
            "cost": by_cost,
            "area": by_area,
            "floors": by_floors,
        }

        sort_func = mapping[key]

        return self._district.sort_by(sort_func, reverse)

    def make_contract(self, address: str) -> None:
        house = self._get_house_by_address(address)
        if not house:
            raise HouseNotFoundError(address)

        house.make_contract()

    def reset_house(self, address: str) -> None:
        house = self._get_house_by_address(address)
        if not house:
            raise HouseNotFoundError(address)

        house.reset()

    def load_data(self) -> None:
        try:
            data = load(self._storage_path) or []

            for item in data:
                house = dict_to_house(item)
                self._district.add(house)

        except FileNotFoundError:
            return

        except Exception as error:
            raise StorageError("load", self._storage_path) from error

    def save_data(self) -> None:
        try:
            data = [house_to_dict(h) for h in self._district.get_all()]
            save(data, self._storage_path)

        except Exception as error:
            raise StorageError("save", self._storage_path) from error

    def district(self) -> HousesDistrict:
        return self._district

    def show_all(self):
        return self._district

    def list_to_table(self, list_table: list[House]) -> str:
        header = f"| {'Address':<24} | {'Floors':<6} | {'Area(m²)':<8} | {'Cost($/month)':<14} | {'MinRent(months)':<15} | {'Rented':<6} |"
        separator = "-" * len(header)

        rows = "\n".join(
            f"| {h.address:<24} | "
            f"{h.floors:<6} | "
            f"{h.area:<8} | "
            f"{h.cost:<14} | "
            f"{h.min_time_rent:<15} | "
            f"{str(h.rented):<6} |"
            for h in list_table
        )

        return f"{header}\n{separator}\n{rows}"

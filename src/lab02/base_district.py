from src.libs.models.base_house import House
from src.libs.interfaces.pt_cl_interfaces import (
    RentIncome,
    ComfortIndex,
    RentalFeasibilityIndex,
)
from src.libs.validators.base_house import validate_type, VALIDATORS
from src.libs.config.config import FIELD_MAP
from typing import Callable, Any, Iterator


class HousesDistrict:
    def __init__(self, name: str, items: list[House] | None = None) -> None:
        self._name: str = name
        self._items: list[House] = items or []

    def add(self, other: House) -> None:
        validate_type(other, House)

        for item in self._items:
            if item.address == other.address:
                raise ValueError(f"Object is not added! Object is in {self._name}!")
        self._items.append(other)

    def remove(self, item: House) -> None:
        validate_type(item, House)

        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError(f"Object is not removed! Object is not in {self._name}!")

    def remove_at(self, index: int) -> None:
        accept_index = len(self._items)
        if index < -accept_index or index >= accept_index:
            raise IndexError("Invalid index")
        del self._items[index]

    def get_all(self) -> list[House]:
        return self._items.copy()

    def __getitem__(self, index: int) -> House:
        accept_index = len(self._items)
        if index < -accept_index or index >= accept_index:
            raise IndexError("Invalid index")
        return self._items[index]

    def get_not_rented(self) -> list[House]:
        result: list[House] = []
        for item in self._items:
            if not item.rented:
                result.append(item)
        return result

    def get_private(self) -> list[House]:
        return [item for item in self._items if isinstance(item, ComfortIndex)]

    def get_commercial(self) -> list[House]:
        return [
            item for item in self._items if isinstance(item, RentalFeasibilityIndex)
        ]

    def get_rent_income_objects(self) -> list[House]:
        return [item for item in self._items if isinstance(item, RentIncome)]

    def filter_by(self, predicate: Callable[[House], bool]) -> list[House]:
        filtered = list(filter(predicate, self._items))
        return HousesDistrict(self._name, filtered)

    def sort_by(self, key_func: Callable[[House], Any], reverse: bool = False) -> None:
        sorted_houses = sorted(self._items, key=key_func, reverse=reverse)
        return HousesDistrict(self._name, sorted_houses)

    def find_by(self, field: str, value: Any) -> list[House]:
        if not self._items:
            return []

        if field not in FIELD_MAP:
            raise AttributeError(f"Unknown field: {field}")

        field = FIELD_MAP[field]
        validator = VALIDATORS.get(field)

        if validator:
            validator(value)

        return [item for item in self._items if getattr(item, field, None) == value]

    def apply(self, func: Callable[[House], Any]) -> None:
        for item in self._items:
            func(item)
        return self

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[House]:
        return iter(self._items)

    def __str__(self) -> str:
        header = f"| {'Address':<24} | {'Floors':<6} | {'Area(m²)':<8} | {'Cost($/month)':<14} | {'MinRent(months)':<15} | {'Rented':<6} |"
        separator = "-" * len(header)

        header_main = f"| {self._name:^{len(header) - 4}} |"

        rows = "\n".join(
            f"| {h.address:<24} | "
            f"{h.floors:<6} | "
            f"{h.area:<8} | "
            f"{h.cost:<14} | "
            f"{h.min_time_rent:<15} | "
            f"{str(h.rented):<6} |"
            for h in self._items
        )

        return f"{header_main}\n{separator}\n{header}\n{separator}\n{rows}"

    def __repr__(self) -> str:
        return f"HousesDistrict(name={self._name!r}, items={self._items!r})"

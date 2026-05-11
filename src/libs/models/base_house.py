from abc import ABC, abstractmethod
from src.libs.validators.base_house import (
    validate_address,
    validate_floors,
    validate_area,
    validate_cost,
    validate_min_time_rent,
    validate_rented,
)


class House(ABC):
    WEIGHTS: dict[str, float] = {}  # for efficiency index

    def __init__(
        self,
        address: str,
        floors: int,
        area: float | int,
        cost: float | int,
        min_time_rent: int,
        rented: bool,
    ) -> None:
        self._address: str = validate_address(address)
        self._floors: int = validate_floors(floors)
        self._area: float | int = validate_area(area)
        self._cost: float | int = validate_cost(cost)
        self._min_time_rent: int = validate_min_time_rent(min_time_rent)
        self._rented: bool = validate_rented(rented)

    @property
    def address(self) -> str:
        return self._address

    @property
    def floors(self) -> int:
        return self._floors

    @property
    def area(self) -> float | int:
        return self._area

    @property
    def cost(self) -> float | int:
        return self._cost

    @cost.setter
    def cost(self, value: float | int) -> None:
        value = validate_cost(value)
        if self._rented:
            raise ValueError("You cannot change cost when house is rented!")
        if self._cost == value:
            raise ValueError("New value of cost is the same as old!")
        self._cost = value

    @property
    def min_time_rent(self) -> int:
        return self._min_time_rent

    @min_time_rent.setter
    def min_time_rent(self, value: int) -> None:
        value = validate_min_time_rent(value)
        if self._rented:
            raise ValueError("You cannot change minimal time of rent when house is rented!")
        elif self._min_time_rent == value:
            raise ValueError("New value of minimal time rent is the same as old!")
        self._min_time_rent = value

    @property
    def rented(self) -> bool:
        return self._rented

    @rented.setter
    def rented(self, value: bool) -> None:
        value = validate_rented(value)
        if self._rented == value:
            raise ValueError("New value of rented is the same as old!")
        self._rented = value

    def make_contract(self) -> None:
        if self._rented:
            raise ValueError("House had already rented!")
        self._rented = True

    def cost_rent_time(self) -> float | int:
        return self._cost * self._min_time_rent

    @abstractmethod
    def value_efficiency_index(self) -> float | int:
        ...

    def __str__(self) -> str:
        return (
            f"Address: {self._address}, "
            f"Floors: {self._floors}, "
            f"Area: {self._area} m², "
            f"Cost: {self._cost}$/month, "
            f"Min rent: {self._min_time_rent} months, "
            f"Rented: {self._rented}"
        )

    def __repr__(self) -> str:
        return (
            f"House(address={self._address!r}, floors={self._floors}, "
            f"area={self._area}, cost={self._cost}, "
            f"min_time_rent={self._min_time_rent}, rented={self._rented})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, House):
            return False
        return self._area == other._area and self._cost == other._cost
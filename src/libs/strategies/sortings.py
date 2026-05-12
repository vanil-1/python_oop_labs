from typing import Protocol


class HouseBase(Protocol):
    address: str
    floors: int
    area: float | int
    cost: float | int
    min_time_rent: int


class HasEfficiency(Protocol):
    def value_efficiency_index(self) -> float | int: ...


class HasComfortIndex(Protocol):
    def comfort_index(self) -> float | int: ...


class HasRentalFeasibilityIndex(Protocol):
    def rental_feasibility_index(self) -> float | int: ...


def by_address(house: HouseBase) -> str:
    return house.address


def by_floors(house: HouseBase) -> int:
    return house.floors


def by_area(house: HouseBase) -> float | int:
    return house.area


def by_cost(house: HouseBase) -> float | int:
    return house.cost


def by_min_time_rent(house: HouseBase) -> int:
    return house.min_time_rent


def by_efficiency(house: HasEfficiency) -> float | int:
    return house.value_efficiency_index()


def by_comfort(house: HasComfortIndex) -> float | int:
    return getattr(house, "comfort_index", lambda: 0)()


def by_rental_feasibility(house: HasRentalFeasibilityIndex) -> float | int:
    return getattr(house, "rental_feasibility_index", lambda: 0)()

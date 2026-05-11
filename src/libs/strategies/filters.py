from typing import Protocol


class Rentable(Protocol):
    rented: bool

class ComfortIndex(Protocol):
    def comfort_index(self) -> float | int: ...

class RentalFeasibilityIndex(Protocol):
    def rental_feasibility_index(self) -> float | int: ...


def is_not_rented(house: Rentable) -> bool:
    return not house.rented

def has_comfort_capability(house: ComfortIndex) -> list[ComfortIndex]:
    return hasattr(house, "comfort_index")

def has_rental_feasibility_index(house: RentalFeasibilityIndex) -> list[RentalFeasibilityIndex]:
      return hasattr(house, "rental_feasibility_index")
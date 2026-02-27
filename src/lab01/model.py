import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from validate import *


class House:
    def __init__(
        self,
        address: str,
        floors: int,
        area: float | int,
        cost: float | int,
        min_time_rent: int,
        rented: bool,
    ):
        self._address = validate_address(address)
        self._floors = validate_floors(floors)
        self._area = validate_area(area)
        self._cost = validate_cost(cost)
        self._min_time_rent = validate_min_time_rent(min_time_rent)
        self._rented = validate_rented(rented)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        value = validate_cost(value)
        if self._rented:
            raise Warning("You cannot change cost when house is rented!")
        elif self._rented == value:
            raise Warning("New value of cost is the same as old!")
        else:
            self._cost = value

    @property
    def rented(self):
        return self._rented

    @rented.setter
    def rented(self, value):
        value = validate_rented(value)
        if self._rented == value:
            raise Warning("New value of rented is the same as old!")
        else:
            self._rented = value

    @property
    def min_time_rent(self):
        return self._min_time_rent

    @min_time_rent.setter
    def min_time_rent(self, value):
        value = validate_min_time_rent(value)
        if self._rented:
            raise Warning(
                "You cannot change minimal time of rent when house is rented!"
            )
        elif self._min_time_rent == value:
            raise Warning("New value of minimal time rent is the same as old!")
        else:
            self._min_time_rent = value

    def make_contract(self):
        if self._rented:
            return "House had already rented!"
        else:
            self._rented = True
            return f"House on the {self._address} is rented successfully!"

    def cost_rent_time(self):
        return f"Cost of {self._min_time_rent} months is {self._cost * self._min_time_rent}$."

    def __str__(self):
        header = f"| {'Address':<24} | {'Floors':<6} | {'Area(m²)':<6} | {'Cost($/month)':<14} | {'MinRent(months)':<15} | {'Rented':<6} |"
        separator = "-" * len(header)
        row = f"| {self._address:<24} | {self._floors:<6} | {self._area:<8} | {self._cost:<14} | {self._min_time_rent:<15} | {self._rented!s:<6} |"
        return f"{header}\n{separator}\n{row}"

    def __repr__(self):
        return f"House(address={self._address!r}, floors={self._floors}, area={self._area}, cost={self._cost}, min_time_rent={self._min_time_rent},rented={self._rented})"

    def __eq__(self, other):
        if not isinstance(other, House):
            return False
        return (
            "Areas are equal. "
            if self._area == other._area
            else f"Areas are not equal! "
        ) + (
            "Costs are equal." if self._cost == other._cost else f"Costs are not equal!"
        )

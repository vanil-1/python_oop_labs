from src.libs.validators.base_house import (
    validate_address,
    validate_floors,
    validate_area,
    validate_cost,
    validate_min_time_rent,
    validate_rented,
)


class House:
    WEIGHTS = {}
    
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
    def address(self):
        return self._address

    @property
    def floors(self):
        return self._floors

    @property
    def area(self):
        return self._area

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        value = validate_cost(value)
        if self._rented:
            raise ValueError("You cannot change cost when house is rented!")
        elif self._cost == value:
            raise ValueError("New value of cost is the same as old!")
        else:
            self._cost = value

    @property
    def min_time_rent(self):
        return self._min_time_rent

    @min_time_rent.setter
    def min_time_rent(self, value):
        value = validate_min_time_rent(value)
        if self._rented:
            raise ValueError(
                "You cannot change minimal time of rent when house is rented!"
            )
        elif self._min_time_rent == value:
            raise ValueError("New value of minimal time rent is the same as old!")
        else:
            self._min_time_rent = value

    @property
    def rented(self):
        return self._rented

    @rented.setter
    def rented(self, value):
        value = validate_rented(value)
        if self._rented == value:
            raise ValueError("New value of rented is the same as old!")
        else:
            self._rented = value

    def make_contract(self):
        if self._rented:
            raise ValueError("House had already rented!")
        else:
            self._rented = True
            return f"House on the {self._address} is rented successfully!"

    def cost_rent_time(self):
        return self._cost * self._min_time_rent

    def __str__(self):
        return (
            f"Address: {self._address}, "
            f"Floors: {self._floors}, "
            f"Area: {self._area} m², "
            f"Cost: {self._cost}$/month, "
            f"Min rent: {self._min_time_rent} months, "
            f"Rented: {self._rented}"
        )

    def __repr__(self):
        return f"House(address={self._address!r}, floors={self._floors}, area={self._area}, cost={self._cost}, min_time_rent={self._min_time_rent},rented={self._rented})"

    def __eq__(self, other):
        if not isinstance(other, House):
            return False
        return self._area == other._area and self._cost == other._cost

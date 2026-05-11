from src.libs.models.base_house import House
from src.lab04.interfaces import (
    RentIncome,
    Reset,
    HasComfortIndex,
    HasRentalFeasibilityIndex,
)
from src.libs.validators.common_house import validate_people_count
from src.libs.validators.private_house import (
    validate_land_area,
    validate_heating_type,
)
from src.libs.validators.commercial_house import (
    validate_usage_type,
    validate_operational_area,
)


class PrivateHouse(House, RentIncome, Reset, HasComfortIndex):
    WEIGHTS = {
        "S": 0.25,
        "H": 0.3,
        "C": 0.25,
        "F": 0.2,
    }  # weights for count comfort_index()
    SENSITIVITY_HEATING = {"gas": 1.0, "electric": 0.7, "stove": 0.4}

    def __init__(
        self,
        address: str,
        floors: int,
        area: float | int,
        cost: float | int,
        min_time_rent: int,
        rented: bool,
        land_area: int | float,
        heating_type: str,
        occupants_count: int,
    ) -> None:
        super().__init__(
            address=address,
            floors=floors,
            area=area,
            cost=cost,
            min_time_rent=min_time_rent,
            rented=rented,
        )

        self._land_area = validate_land_area(land_area)
        self._heating_type = validate_heating_type(heating_type)
        self._occupants_count = validate_people_count(occupants_count)

    @property
    def occupants_count(self) -> int:
        return self._occupants_count

    @occupants_count.setter
    def occupants_count(self, value: int) -> None:
        self._occupants_count = validate_people_count(value)

    def comfort_index(self) -> float | int:
        area_balance = (
            1 - abs((self._area / self._land_area) - 0.3)
        ) / 0.3  # cofficient area: area / land_area
        S = 0.5 * area_balance  # square index

        H = (self.SENSITIVITY_HEATING[self._heating_type]) * (
            1 / (1 + 0.5 * self._occupants_count)
        )  # heating_type index
        C = 1 / (1 + (self._cost / 1000))  # cost index
        F = 1 - 0.2 * abs(self._floors - 2)  # floors index

        ci = (
            self.WEIGHTS["S"] * S
            + self.WEIGHTS["H"] * H
            + self.WEIGHTS["C"] * C
            + self.WEIGHTS["F"] * F
        )

        return max(0, min(ci, 1))

    def value_efficiency_index(self) -> float | int:
        return self.comfort_index()

    def get_rent_income(self) -> float:
        gross = self._cost * self._min_time_rent
        tax = gross * 0.08
        utilities = self._occupants_count * 120

        return gross - (tax + utilities)

    def reset(self) -> None:
        self._rented = False
        self._cost = self._area * 50
        self._min_time_rent = 1
        self._occupants_count = 1


class CommercialHouse(House, RentIncome, Reset, HasRentalFeasibilityIndex):
    WEIGHTS = {"S": 0.4, "U": 0.3}  # weights for count rental_feasibility_index()
    SENSITIVITY_USAGE_TYPE = {
        "office": 0.6,
        "retail": 0.8,
        "warehouse": 0.9,
        "hotel": 0.7,
    }  # usage type sensitivity from area

    def __init__(
        self,
        address: str,
        floors: int,
        area: float | int,
        cost: float | int,
        min_time_rent: int,
        rented: bool,
        usage_type: str,
        operational_area: float | int,
        customers_average_count: int,
    ):
        super().__init__(
            address=address,
            floors=floors,
            area=area,
            cost=cost,
            min_time_rent=min_time_rent,
            rented=rented,
        )

        self._usage_type = validate_usage_type(usage_type)
        self._operational_area = validate_operational_area(operational_area)
        self._customers_average_count = validate_people_count(customers_average_count)

    @property
    def customers_average_count(self) -> int:
        return self._customers_average_count

    @customers_average_count.setter
    def customers_average_count(self, value: int) -> None:
        self._customers_average_count = validate_people_count(value)

    @property
    def operational_area(self) -> float | int:
        return self._operational_area

    @operational_area.setter
    def operational_area(self, value: float | int) -> None:
        self._operational_area = validate_operational_area(value)

    def rental_feasibility_index(self) -> float | int:
        S = 1 - (abs((self._operational_area / self._area) - 0.7) / 0.7)
        sensitivity = self.SENSITIVITY_USAGE_TYPE[self._usage_type]
        U = 1 - (sensitivity * abs(S - 0.7))

        rfi = self.WEIGHTS["S"] * S + self.WEIGHTS["U"] * U

        return max(0, min(rfi, 1))

    def value_efficiency_index(self) -> float | int:
        return self.rental_feasibility_index()

    def get_rent_income(self) -> float:
        gross = self._cost * self._min_time_rent
        tax = gross * 0.15
        usage_multiplier = self.SENSITIVITY_USAGE_TYPE[self._usage_type]
        demand_factor = 1 + (self._customers_average_count / 100) * usage_multiplier

        return gross * demand_factor - tax

    def reset(self) -> None:
        self._rented = False
        self._cost = self._area * 70
        self._min_time_rent = 12
        self._customers_average_count = 5
        self._operational_area = 20

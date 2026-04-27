from src.libs.models.base_house import House
from src.libs.validators.common_house import validate_people_count
from src.libs.validators.private_house import (
    validate_land_area,
    validate_heating_type,
)

class PrivateHouse(House):
    WEIGHTS = {'S': 0.25, 'H': 0.3, 'C': 0.25, 'F': 0.2} # weights for count comfort_index()
    SENSITIVITY_HEATING = {'gas': 1.0, 'electric': 0.7, 'stove': 0.4}

    def __init__(self, 
            address: str,
            floors: int,
            area: float | int,
            cost: float | int,
            min_time_rent: int,
            rented: bool,
            land_area: int|float, 
            heating_type: str,
            occupants_count: int):
        super().__init__(address = address,
                    floors = floors,
                    area = area,
                    cost = cost,
                    min_time_rent = min_time_rent,
                    rented = rented)
        
        self._land_area = validate_land_area(land_area)
        self._heating_type = validate_heating_type(heating_type)
        self._occupants_count = validate_people_count(occupants_count)

    def comfort_index(self):
        area_balance = (1 - abs((self._area / self._land_area) - 0.3)) / 0.3 # cofficient area: area / land_area
        S = 0.5 * area_balance # square index

        H = (self.SENSITIVITY_HEATING[self._heating_type]) * (1 / (1 + 0.5 * self._occupants_count)) # heating_type index
        C = 1 / (1 + (self._cost / 1000)) # cost index
        F = 1 - 0.2 * abs(self._floors - 2) # floors index

        ci = (self.WEIGHTS['S'] * S +
                self.WEIGHTS['H'] * H +
                self.WEIGHTS['C'] * C +
                self.WEIGHTS['F'] * F)
        
        return max(0, min(ci, 1))

    def value_efficiency_index(self):
        return self.comfort_index()

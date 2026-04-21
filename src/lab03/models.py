from src.lab03.base import House
from src.libs.validators.child_validate import (
    validate_land_area,
    validate_heating_type,
    validate_usage_type,
    validate_operational_area,
    validate_people_count,
    validate_solo_area,
    validate_budget,
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

    def comfort_index(self, solo_area: int|float):
        solo_area = validate_solo_area(solo_area)

        area_balance = (1 - abs((self._area / self._land_area) - 0.3)) / 0.3 # cofficient area: area / land_area
        required_area = solo_area * self._occupants_count # how many occupants need area
        cofficient_size = 1 - (abs(self._area - required_area) / required_area) # cofficient area: area / required_area
        S = 0.5 * (area_balance + cofficient_size) # square index

        H = (self.SENSITIVITY_HEATING[self._heating_type]) * (1 / (1 + 0.5 * self._occupants_count)) # heating_type index
        C = 1 / (1 + (self._cost / 1000)) # cost index
        F = 1 - 0.2 * abs(self._floors - 2) # floors index

        ci = (self.WEIGHTS['S'] * S +
                self.WEIGHTS['H'] * H +
                self.WEIGHTS['C'] * C +
                self.WEIGHTS['F'] * F)
        
        return max(0, min(ci, 1))
    
    def cost_rent_time(self):
        return super().cost_rent_time() + f"Cost for one person is {(self._cost * self._min_time_rent) / self._occupants_count}$."


class CommercialHouse(House):
    WEIGHTS = {'S': 0.4, 'U': 0.3, 'B': 0.4} # weights for count rental_feasibility_index()
    SENSITIVITY_USAGE_TYPE = { 
        "office": 0.6,
        "retail": 0.8,
        "warehouse": 0.9,
        "hotel": 0.7,
    } # usage type sensitivity from area

    def __init__(self, 
            address: str,
            floors: int,
            area: float | int,
            cost: float | int,
            min_time_rent: int,
            rented: bool, 
            usage_type: str, 
            operational_area: int|float,
            customers_average_count: int):
        super().__init__(address = address,
                    floors = floors,
                    area = area,
                    cost = cost,
                    min_time_rent = min_time_rent,
                    rented = rented)
        
        self._usage_type = validate_usage_type(usage_type)
        self._operational_area = validate_operational_area(operational_area)
        self._customers_average_count = validate_people_count(customers_average_count)

    def rental_feasibility_index(self, budget: int|float):
        budget = validate_budget(budget)
        S = 1 - (abs((self._operational_area / self._area) - 0.7) / 0.7)
        sensitivity = self.SENSITIVITY_USAGE_TYPE[self._usage_type]
        U = 1 - (sensitivity * abs(S - 0.7))
        B = abs(budget - self._cost) / budget

        rfi = (self.WEIGHTS['S'] * S +
            self.WEIGHTS['U'] * U +
            self.WEIGHTS['B'] * B)
        
        return max(0, min(rfi, 1))
    
    def cost_rent_time(self):
        return super().cost_rent_time() + f"You need get {(self._cost * self._min_time_rent) / self._customers_average_count}$ from {self._customers_average_count} to pay rent."
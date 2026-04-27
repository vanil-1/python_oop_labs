from src.libs.models.base_house import House
from src.libs.validators.common_house import validate_people_count
from src.libs.validators.commercial_house import (
    validate_usage_type,
    validate_operational_area,
)

class CommercialHouse(House):
    WEIGHTS = {'S': 0.4, 'U': 0.3} # weights for count rental_feasibility_index()
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

    def rental_feasibility_index(self):
        S = 1 - (abs((self._operational_area / self._area) - 0.7) / 0.7)
        sensitivity = self.SENSITIVITY_USAGE_TYPE[self._usage_type]
        U = 1 - (sensitivity * abs(S - 0.7))


        rfi = (self.WEIGHTS['S'] * S +
            self.WEIGHTS['U'] * U)
        
        return max(0, min(rfi, 1))
    
    def value_efficiency_index(self):
        return self.rental_feasibility_index()
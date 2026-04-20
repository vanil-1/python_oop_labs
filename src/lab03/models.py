from src.lab03.base import House
from src.libs.validators.child_validate import (
    validate_land_area,
    validate_heating_type,
    validate_usage_type,
    validate_rentable_area,
)

class PrivateHouse(House):
    def __init__(self, land_area, heating_type, **kwargs):
        super().__init__(**kwargs)
        self._land_area = validate_land_area(land_area)
        self._heating_type = validate_heating_type(heating_type)

    def comfort_index(self):
        pass


class CommercialHouse(House):
    def __init__(self, usage_type, rentable_area, **kwargs):
        super().__init__(**kwargs)
        self._usage_type = validate_usage_type(usage_type)
        self._rentable_area = validate_rentable_area(rentable_area)

    def profitability_index(self):
        pass
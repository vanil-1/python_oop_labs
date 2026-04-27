from src.libs.models.private_house import PrivateHouse
from src.libs.models.commercial_house import CommercialHouse
 

FIELD_MAP = {
    "address": "address",
    "floors": "floors",
    "area": "area",
    "cost": "cost",
    "min_time_rent": "min_time_rent",
    "rented": "rented",
}

CLASS_MAP = {
    "private": PrivateHouse,
    "commercial": CommercialHouse
}
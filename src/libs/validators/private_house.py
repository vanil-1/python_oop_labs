def validate_land_area(land_area: float | int) -> float | int:
    if not isinstance(land_area, float | int):
        raise TypeError("Land Area must be float or int!")
    
    if not (100 <= land_area <= 50000):
        raise ValueError("Land Area must be more than 100 and less than 50000!")
    
    return land_area


def validate_heating_type(heating_type: str) -> str:
    if not isinstance(heating_type, str):
        raise TypeError("Heating Type must be string!")
    
    heating_type = heating_type.casefold()

    if not (heating_type in ['gas', 'electric', 'stove']):
        raise ValueError("Heating Type must be gas, elictric or stove!")
    
    return heating_type

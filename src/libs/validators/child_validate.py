def validate_land_area(land_area: int|float):
    if not isinstance(land_area, int|float):
        raise TypeError("Land Area must be int or float!")
    
    if not (100 <= land_area <= 50000):
        raise ValueError("Land Area must be more than 100 and less than 50000!")
    
    return land_area

def validate_heating_type(heating_type: str):
    if not isinstance(heating_type, str):
        raise TypeError("Heating Type must be string!")
    
    heating_type = heating_type.casefold()

    if not (heating_type in ['gas', 'electric', 'stove']):
        raise ValueError("Heating Type must be gas, elictric or stove!")
    
    return heating_type

def validate_usage_type(usage_type: str):
    if not isinstance(usage_type, str):
        raise TypeError("Usage Type must be string!")
    
    usage_type = usage_type.casefold()

    if not (usage_type in ['office', 'retail', 'warehouse', 'hotel']):
        raise ValueError("Usage Type must be office, retail, warehouse or hotel!")
    
    return usage_type

def validate_rentable_area(rentable_are: int|float):
    if not isinstance(rentable_are, int|float)
        raise TypeError("Rentable Area must be int or float!")
    
    if not (10 <= rentable_are <= 100000):
        raise  ValueError("Rentable Area must be more than 10 and less than 100000!")
    
    return rentable_are
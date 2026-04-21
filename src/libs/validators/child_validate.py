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

def validate_people_count(people_count: int):
    if not isinstance(people_count, int):
        raise TypeError("People count must be int!")
    
    if not (0 < people_count < 41):
        raise ValueError("People count must be more than 0 and less than 41!")
    
    return people_count

def validate_solo_area(solo_area: int|float):
    if not isinstance(solo_area, int|float):
        raise TypeError("Solo Area must be int or float!")
    
    if not (10 <= solo_area <= 60):
        raise ValueError("Solo Area must be more then 10 and less than 60!")
    
    return solo_area

def validate_usage_type(usage_type: str):
    if not isinstance(usage_type, str):
        raise TypeError("Usage Type must be string!")
    
    usage_type = usage_type.casefold()

    if not (usage_type in ['office', 'retail', 'warehouse', 'hotel']):
        raise ValueError("Usage Type must be office, retail, warehouse or hotel!")
    
    return usage_type

def validate_operational_area(operational_area: int|float):
    if not isinstance(operational_area, int|float)
        raise TypeError("Rentable Area must be int or float!")
    
    if not (10 <= operational_area <= 100000):
        raise  ValueError("Rentable Area must be more than 10 and less than 100000!")
    
    return operational_area

def validate_budget(budget: int|float):
    if not isinstance(budget, int|float):
        raise TypeError("Budget must be int or float!")
    
    if budget < 100:
        raise ValueError("Budget must be more than 100!")

    return budget
def validate_usage_type(usage_type: str) -> str:
    if not isinstance(usage_type, str):
        raise TypeError("Usage Type must be string!")
    
    usage_type = usage_type.casefold()

    if not (usage_type in ['office', 'retail', 'warehouse', 'hotel']):
        raise ValueError("Usage Type must be office, retail, warehouse or hotel!")
    
    return usage_type


def validate_operational_area(operational_area: float | int) -> float | int:
    if not isinstance(operational_area, float | int):
        raise TypeError("Rentable Area must be float or int!")
    
    if not (10 <= operational_area <= 100000):
        raise  ValueError("Rentable Area must be more than 10 and less than 100000!")
    
    return operational_area

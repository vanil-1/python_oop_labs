def validate_people_count(people_count: int) -> int:
    if not isinstance(people_count, int):
        raise TypeError("People count must be int!")
    
    if not (0 < people_count < 41):
        raise ValueError("People count must be more than 0 and less than 41!")
    
    return people_count

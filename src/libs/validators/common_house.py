def validate_people_count(people_count: int) -> int:
    if not isinstance(people_count, int):
        raise TypeError("People count must be int!")

    if not (0 < people_count < 41):
        raise ValueError("People count must be between 1 and 40!")

    return people_count

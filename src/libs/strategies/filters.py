def is_not_rented(house):
    return not house.rented


def has_comfort_capability(house):
    return hasattr(house, "comfort_index")


def has_rental_feasibility_index(house):
    return hasattr(house, "rental_feasibility_index")

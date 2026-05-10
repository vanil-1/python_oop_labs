def by_address(house):
    return house.address


def by_floors(house):
    return house.floors


def by_area(house):
    return house.area


def by_cost(house):
    return house.cost


def by_min_time_rent(house):
    return house.min_time_rent


def by_efficiency(house):
    return house.value_efficiency_index()


def by_comfort(house):
    return getattr(house, "comfort_index", lambda: 0)()


def by_rental_feasibility(house):
    return getattr(house, "rental_feasibility_index", lambda: 0)()

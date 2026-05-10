def make_cost_filter(max_cost):
    def predicate(house):
        return house.cost <= max_cost

    return predicate


def make_area_filter(min_area):
    def predicate(house):
        return house.area >= min_area

    return predicate

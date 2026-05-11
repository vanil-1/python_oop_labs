from typing import Callable, Protocol

class HasCostArea(Protocol):
    cost: float
    area: float

def make_cost_filter(max_cost) -> Callable[[HasCostArea], bool]:
    def predicate(house) -> bool:
        return house.cost <= max_cost

    return predicate


def make_area_filter(min_area) -> Callable[[HasCostArea], bool]:
    def predicate(house) -> bool:
        return house.area >= min_area

    return predicate

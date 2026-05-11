from src.libs.converters.pt_cl_convert import convert_pr_cl_to_list
from src.libs.models.models_map import CLASS_MAP
from src.libs.collections.base_district import HousesDistrict

from src.lab05.strategies import (
    RenovationStrategy,
    InvestmentScoreStrategy,
)

from src.lab05.factories import (
    make_cost_filter,
)

from src.lab05.filters import (
    is_not_rented,
    has_comfort_capability,
)

from src.lab05.sortings import (
    by_cost,
    by_area,
    by_comfort,
)


def main():
    print("\n=== SCENARIO 1: CHAIN FILTER → SORT → APPLY ===\n")

    houses = convert_pr_cl_to_list(CLASS_MAP, "data/lab05/data.json")
    district = HousesDistrict("Neo District", houses)

    result = (
        district.filter_by(is_not_rented)
        .filter_by(has_comfort_capability)
        .sort_by(by_cost)
        .apply(RenovationStrategy(1.1))
    )

    print("After full chain:")
    for h in result:
        print(h.address, h.cost)

    print("\n=== SCENARIO 2: MAP + FACTORY + COMPARISON ===\n")

    cost_filter = make_cost_filter(1000)
    filtered = district.filter_by(cost_filter)

    print("Factory filter result:")
    for h in filtered:
        print(h.address, h.cost)

    print("\nMAP transformations (real usage):")

    names = list(map(lambda h: h.address, district))
    costs_with_tax = list(map(lambda h: h.cost * 1.2, district))

    print("Names:", names)
    print("Costs + tax:", costs_with_tax)

    print("\n=== SCENARIO 3: STRATEGIES + CALLABLE + POLYMORPHISM ===\n")

    print("SORT BY COST:")
    print([h.address for h in district.sort_by(by_cost)])

    print("SORT BY AREA:")
    print([h.address for h in district.sort_by(by_area)])

    print("SORT BY COMFORT (child capability):")
    print([h.address for h in district.sort_by(by_comfort)])

    print("\nCALLABLE STRATEGY (Investment Score):")

    investment = InvestmentScoreStrategy()
    scores = list(map(investment, district))

    for h, s in zip(district, scores):
        print(h.address, s)


if __name__ == "__main__":
    main()

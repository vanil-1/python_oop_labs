from src.libs.models.models_map import CLASS_MAP
from src.libs.converters.pt_cl_convert import convert_pr_cl_to_list
from src.lab06.container import ComfortIndex, RentalFeasibilityIndex, TypedCollection


def scenario_generic_collection() -> None:
    print("\n===== SCENARIO 1 =====")

    numbers: TypedCollection[int] = TypedCollection("numbers")

    numbers.add(10)
    numbers.add(20)
    numbers.add(30)

    print(numbers.get_all())
    print(len(numbers))


def scenario_find_filter_map() -> None:
    print("\n===== SCENARIO 2 =====")

    houses: TypedCollection[ComfortIndex] = TypedCollection("houses")

    collection_houses = convert_pr_cl_to_list(CLASS_MAP, "data/lab06/data_private.json")

    for house in collection_houses:
        houses.add(house)

    print("find ok:", houses.find(lambda h: h.cost > 900))
    print("find none:", houses.find(lambda h: h.cost > 99999))
    print("filter:", houses.filter(lambda h: h.cost < 1000))

    names: list[str] = houses.map(lambda h: h.address)
    costs: list[float] = houses.map(lambda h: h.cost)

    print("names:", names)
    print("costs:", costs)


def scenario_map_type_change() -> None:
    print("\n===== SCENARIO 3 =====")

    houses: TypedCollection[ComfortIndex] = TypedCollection("houses")

    collection_houses = convert_pr_cl_to_list(CLASS_MAP, "data/lab06/data_private.json")

    for house in collection_houses:
        houses.add(house)

    addresses: list[str] = houses.map(lambda h: h.address)
    comforts: list[float] = houses.map(lambda h: h.comfort_index())

    print(addresses)
    print(comforts)


def scenario_comfort_index() -> None:
    print("\n===== SCENARIO 4 =====")

    col: TypedCollection[ComfortIndex] = TypedCollection("comfortindex")
    collection_houses = convert_pr_cl_to_list(CLASS_MAP, "data/lab06/data_private.json")

    for house in collection_houses:
        col.add(house)

    for item in col.get_all():
        print(item.comfort_index())


def scenario_rental_feasibility_index() -> None:
    print("\n===== SCENARIO 5 =====")

    col: TypedCollection[RentalFeasibilityIndex] = TypedCollection(
        "rentalfeasibilityindex"
    )
    collection_houses = convert_pr_cl_to_list(
        CLASS_MAP, "data/lab06/data_commercial.json"
    )

    for house in collection_houses:
        col.add(house)

    for item in col.get_all():
        print(item.rental_feasibility_index())


def main():
    scenario_generic_collection()
    scenario_find_filter_map()
    scenario_map_type_change()
    scenario_comfort_index()
    scenario_rental_feasibility_index()


if __name__ == "__main__":
    main()

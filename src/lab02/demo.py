from src.libs.models.house_model import House
from src.lab02.collection import HousesDistrict
from src.libs.converters.converter import convert_to_list


def print_block(title: str):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def safe_run(fn):
    try:
        fn()
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {e}")


house_list = convert_to_list(House, "data/lab02/data.json")
district = HousesDistrict("Green Park District", house_list)

test_house = House(
    address="7 cedar lane", floors=2, area=60, cost=220, min_time_rent=2, rented=False
)


def scenario_1():
    print_block("SCENARIO 1: CRUD OPERATIONS")

    print(district, "Initial collection")

    print("\nAdding house...")
    district.add(test_house)
    print(district, "After add()")

    print("\nRemoving house...")
    district.remove(test_house)
    print(district, "After remove()")


def scenario_2():
    print_block("SCENARIO 2: SEARCH & FILTER")

    print("\nFind by address:")
    print(district.find_by("address", "8 pine road"))

    print("\nNot rented houses:")
    print(district.get_not_rented())


def scenario_3():
    print_block("SCENARIO 3: COLLECTION FEATURES")

    print("Length:", len(district))

    print("\nIndexing [0]:")
    print(district[0])

    print("\nIteration:")
    for house in district:
        print(house)

    print_block("Sorting by cost")
    district.sort_by_cost()
    print(district, "After sort")

    print("\nRemove at index 0:")
    district.remove_at(0)
    print(district, "After remove_at")


def scenario_4_errors():
    print_block("SCENARIO 4: ERROR HANDLING DEMO")

    print("\n1) Adding duplicate:")
    safe_run(lambda: district.add(test_house))
    safe_run(lambda: district.add(test_house))

    print("\n2) Wrong type add:")
    safe_run(lambda: district.add("invalid"))

    print("\n3) Invalid index remove:")
    safe_run(lambda: district.remove_at(999))


def main():
    actions = {
        "1": scenario_1,
        "2": scenario_2,
        "3": scenario_3,
        "4": scenario_4_errors,
    }

    while True:
        print("\n" + "=" * 80)
        print("DEMO MENU")
        print("1 - CRUD operations")
        print("2 - Search & filter")
        print("3 - Collection features")
        print("4 - Error handling demo")
        print("0 - Exit")
        print("=" * 80)

        choice = input("Select option: ").strip()

        if choice == "0":
            break

        action = actions.get(choice)

        if action:
            safe_run(action)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()

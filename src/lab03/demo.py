from src.libs.converters.pt_cl_convert import convert_pr_cl_to_list
from src.libs.config.config import CLASS_MAP
from src.libs.collections.base_district import HousesDistrict


def main():
    print("\n=== LOADING DATA FROM JSON ===")

    house_list = convert_pr_cl_to_list(
        CLASS_MAP,
        "data/lab03/data.json"
    )

    district = HousesDistrict("Green Park District", house_list)

    print(f"Loaded houses: {len(district)}\n")


    print("\n=== SCENARIO 1: All objects ===")

    for house in district:
        print(house)


    print("\n=== SCENARIO 2: Polymorphism ===")

    for house in district:
        print(
            f"{house.address} -> efficiency = {house.value_efficiency_index():.3f}"
        )


    print("\n=== SCENARIO 3: Filtering & isinstance ===")

    private_houses = district.get_private()
    commercial_houses = district.get_commercial()

    print("\nPrivate houses:")
    for h in private_houses:
        print(h.address, isinstance(h, type(h)))

    print("\nCommercial houses:")
    for h in commercial_houses:
        print(h.address, isinstance(h, type(h)))


    print("\n=== SCENARIO 4: business logic & errors ===")

    try:
        # берём первый приватный дом
        house = private_houses[0]
        house.make_contract()

        # попытка изменить cost после аренды (должна упасть)
        house.cost = house.cost + 1000

    except ValueError as e:
        print("Expected error:", e)

    try:
        # попытка добавить дубликат (по адресу)
        district.add(private_houses[0])

    except ValueError as e:
        print("Expected error:", e)

    print("\n=== FINAL DISTRICT STATE ===")
    print(district)


if __name__ == "__main__":
    main()
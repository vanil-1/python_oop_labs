from src.libs.converters.pt_cl_convert import convert_pr_cl_to_list
from src.libs.models.models_map import CLASS_MAP
from src.libs.collections.base_district import HousesDistrict
from src.lab04.interfaces import RentIncome, Reset
from src.lab04.services import reset_all, total_income


def main():
    print("\n=== SCENARIO 1: SYSTEM INITIALIZATION (polymorphic loading) ===")

    houses = convert_pr_cl_to_list(CLASS_MAP, "data/lab04/data.json")

    district = HousesDistrict("Neon District", houses)

    print(f"System initialized: {len(district)} objects loaded")

    print("\n=== SCENARIO 2: INTERFACE-BASED BEHAVIOR (RentIncome polymorphism) ===")

    for h in district.get_rent_income_objects():
        print(f"{h.address}: income = {h.get_rent_income():.2f}")

    print("\n=== SCENARIO 3: UNIFIED INTERFACE FUNCTIONS (no direct class usage) ===")

    print("Total district income:")
    print(total_income(district.get_rent_income_objects()))

    print("\nResetting all rentable objects...")
    reset_all(district.get_rent_income_objects())

    print("After reset income check:")
    print(total_income(district.get_rent_income_objects()))

    print("\n=== SCENARIO 4: INTERFACE DETECTION + BEHAVIOR DIFFERENCE ===")

    for obj in district:
        print(
            f"{obj.address} | "
            f"RentIncome={isinstance(obj, RentIncome)} | "
            f"Reset={isinstance(obj, Reset)}"
        )

    print("\nResetting ONLY commercial houses via interface filter")

    for obj in district:
        if (
            isinstance(obj, Reset)
            and hasattr(obj, "get_house_type")
            and obj.get_house_type() == "commercial"
        ):
            obj.reset()

    print("\n=== SCENARIO 5: ARCHITECTURAL VALIDATION (no direct type logic) ===")

    rentable_items = district.get_rent_income_objects()

    sorted_income = sorted(
        rentable_items, key=lambda x: x.get_rent_income(), reverse=True
    )

    print("Top 3 income objects:")
    for obj in sorted_income[:3]:
        print(obj.address, obj.get_rent_income())


if __name__ == "__main__":
    main()

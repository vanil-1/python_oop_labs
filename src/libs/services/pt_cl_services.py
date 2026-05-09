from src.libs.interfaces.pt_cl_interfaces import RentIncome, Reset


def reset_all(items: list[Reset]) -> None:
    for item in items:
        item.reset()


def total_income(items: list[RentIncome]) -> float:
    return sum(item.get_rent_income() for item in items)

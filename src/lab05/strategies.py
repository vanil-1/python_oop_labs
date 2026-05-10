from src.libs.interfaces.pt_cl_interfaces import RentIncome


class RenovationStrategy:
    def __init__(self, coefficient=1.2):
        self.coefficient = coefficient

    def __call__(self, house):
        house.cost = int(house.cost * self.coefficient)


class InvestmentScoreStrategy:
    def __call__(self, house):
        if not isinstance(house, RentIncome):
            return 0

        return house.get_rent_income() * house.value_efficiency_index()

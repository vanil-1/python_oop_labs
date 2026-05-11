from typing import Protocol

class RentIncome(Protocol):
    def get_rent_income(self) -> float: ...
    def value_efficiency_index(self) -> float: ...

class RenovationStrategy:
    def __init__(self, coefficient: float = 1.2):
        self.coefficient = coefficient

    def __call__(self, house: RentIncome) -> None:
        house.cost = int(house.cost * self.coefficient)

class InvestmentScoreStrategy:
    def __call__(self, house: RentIncome) -> float:
        return house.get_rent_income() * house.value_efficiency_index()
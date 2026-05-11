from abc import ABC, abstractmethod

class RentIncome(ABC):
    @abstractmethod
    def get_rent_income(self) -> float:
        pass

class Reset(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

class ComfortIndex(ABC):
    def comfort_index(self) -> float | int:
        pass

class RentalFeasibilityIndex(ABC):
    def rental_feasibility_index(self) -> float | int:
        pass 

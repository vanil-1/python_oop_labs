from abc import ABC, abstractmethod

class RentIncome(ABC):
    @abstractmethod
    def get_rent_income(self) -> float:
        pass

class Reset(ABC):

    @abstractmethod
    def reset(self) -> None:
        pass

class HouseType(ABC):
    @abstractmethod
    def get_house_type(self) -> str:
        pass
from operator import attrgetter
from src.libs.models.house_model import House
from src.libs.validators.validate import validate_type, VALIDATORS
from src.libs.config.config import FIELD_MAP

class HousesDistrict:
    def __init__(self, name: str, items: list[House] | None = None):
        self._name = name
        self._items: list[House] = items or []

    def add(self, other: House):
        validate_type(other, House)

        for item in self._items:
            if item.address == other.address:
                raise ValueError(f"Object is not added! Object is in {self._name}!")
        self._items.append(other)

    def remove(self, item: House):
        validate_type(item, House)

        if item in self._items: self._items.remove(item)
        else: raise ValueError(f"Object is not removed! Object is not in {self._name}!")

    def remove_at(self, index):
        accept_index = len(self._items)
        if index < -accept_index or index >= accept_index:
            raise IndexError("Invalid index")
        del self._items[index]

    def get_all(self):
        return self._items.copy()
    
    def __getitem__(self, index):
        accept_index = len(self._items)
        if index < -accept_index or index >= accept_index:
            raise IndexError("Invalid index")
        return self._items[index]

    def get_not_rented(self):        
        result = []
        for item in self._items:
            if not item.rented:
                result.append(item)
                
        return result
    
    def sort_by_cost(self):
        self._items.sort(key=attrgetter("cost"))

    def find_by(self, field: str, value):
        if not self._items:
            return []
        
        if field not in FIELD_MAP:
            raise AttributeError(f"Unknown field: {field}")
        
        field = FIELD_MAP[field]
        validator = VALIDATORS.get(field)
        
        if validator:
            validator(value)

        result = [item for item in self._items if getattr(item, field, None) == value]
        return result
        
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __str__(self):
        header = f"| {'Address':<24} | {'Floors':<6} | {'Area(m²)':<8} | {'Cost($/month)':<14} | {'MinRent(months)':<15} | {'Rented':<6} |"
        separator = "-" * len(header)

        header_main = f"| {self._name:^{len(header) - 4}} |"

        rows = "\n".join(
        f"| {h.address:<24} | "
        f"{h.floors:<6} | "
        f"{h.area:<8} | "
        f"{h.cost:<14} | "
        f"{h.min_time_rent:<15} | "
        f"{str(h.rented):<6} |"
        for h in self._items
    )

        return f"{header_main}\n{separator}\n{header}\n{separator}\n{rows}" 

    def __repr__(self):
        return f"HousesDistrict(name={self._name!r}, items={self._items!r})"

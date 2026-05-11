from __future__ import annotations
from typing import (
    TypeVar,
    Generic, 
    Callable, 
    Any, 
    Optional, 
    Iterator, 
    Protocol,
    runtime_checkable,
)

@runtime_checkable
class ComfortIndex(Protocol):
    def comfort_index(self) -> float | int: ...

@runtime_checkable
class RentalFeasibilityIndex(Protocol):
    def rental_feasibility_index(self) -> float | int: ... 

C = TypeVar("C", bound = ComfortIndex)
F = TypeVar("F", bound = RentalFeasibilityIndex)

T = TypeVar("T")
R = TypeVar("R")


class TypedCollection(Generic[T]):
    def __init__(self, name: str = "collection", items: list[T] | None = None) -> None:
        self._name: str = name
        self._items: list[T] = items or []

    def add(self, other: T) -> None:
        self._items.append(other)

    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError(f"Object is not removed! Object is not in {self._name}!")
        self._items.remove(item)

    def remove_at(self, index: int) -> None:
        accept_index = len(self._items)

        if index < -accept_index or index >= accept_index:
            raise IndexError("Invalid index")
        del self._items[index]

    def get_all(self) -> list[T]:
        return self._items.copy()

    def __getitem__(self, index: int) -> T:
        accept_index = len(self._items)

        if index < -accept_index or index >= accept_index:
            raise IndexError("Invalid index")
        return self._items[index]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def sort_by(self, key: Callable[[T], Any], reverse: bool = False) -> None:
        self._items.sort(key=key, reverse=reverse)

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]

    def apply(self, func: Callable[[T], Any]) -> None:
        for item in self._items:
            func(item)

    def __str__(self) -> str:
        return f"TypedCollection({self._name}, size = {len(self._items)})"

    def __repr__(self) -> str:
        return f"TypedCollection(name = {self._name!r}, items = {self._items!r})"
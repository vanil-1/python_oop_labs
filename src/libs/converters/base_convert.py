from typing import Type, TypeVar
import json

T = TypeVar("T")


def convert_house_to_list(model_cls: Type[T], path: str) -> list[T]:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    model_list = [model_cls(**item) for item in data]

    return model_list

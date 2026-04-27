from typing import Type, TypeVar
import json

T = TypeVar("T")

def convert_pr_cl_to_list(CLASS_MAP: dict[str, Type[T]], path: str) -> list[T]:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    models_list: list[T] = []

    for item in data:
        obj_type = item.pop("type", None)

        if obj_type is None:
            raise ValueError("Missing 'type' field in JSON!")

        cls = CLASS_MAP.get(obj_type)

        if cls is None:
            raise ValueError(f"Unknown type: {obj_type}")

        models_list.append(cls(**item))

    return models_list

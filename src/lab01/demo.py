import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from model import House


def demo():
    print("\n=== 1. Создание корректного объекта ===")
    house1 = House(
        "12 baker street",
        3,
        120,
        1000,
        6,
        False,
    )
    print(house1)
    print(repr(house1))

    print("\n=== 2. Проверка setter cost ===")
    house1.cost = 1200
    print("New cost:", house1.cost)

    print("\n=== 3. Попытка изменить цену при аренде ===")
    house1.make_contract()
    try:
        house1.cost = 1500
    except Warning as w:
        print("Warning:", w)

    print("\n=== 4. Бизнес-методы ===")
    print(house1.cost_rent_time())

    print("\n=== 5. Проверка rented setter ===")
    try:
        house1.rented = True
    except Warning as w:
        print("Warning:", w)

    print("\n=== 6. Сравнение домов (__eq__) ===")
    house2 = House(
        "5 elm ", 2, 120, 1200, 6, False
    )
    print(house1 == house2)

    print("\n=== 7. Проверка валидации ===")
    try:
        bad_house = House(
            "BAD ADDRESS", 1, 50, 100, 0, "yes"
        )
    except Exception as e:
        print("Validation error:", e)

    print("\n=== 8. Таблица дома ===")
    print(house2)


if __name__ == "__main__":
    demo()

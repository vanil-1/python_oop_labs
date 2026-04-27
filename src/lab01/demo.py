from src.lab01.base_house import House


def normal():
    house = House(
        address="221 baker",
        floors=2,
        area=120,
        cost=1000,
        min_time_rent=6,
        rented=False,
    )

    print(house)
    print(house.cost_rent_time())

    print(house.make_contract())
    print("Rented status:", house.rented)

    return 0


def warnings_errors():
    house = House(
        address="13 elm",
        floors=1,
        area=80,
        cost=800,
        min_time_rent=3,
        rented=False,
    )

    try:
        house.rented = False
    except Warning as w:
        print("Warning:", w)

    house.make_contract()

    try:
        house.cost = 900
    except Warning as w:
        print("Warning:", w)

    try:
        house.min_time_rent = 6
    except Warning as w:
        print("Warning:", w)

    try:
        bad_house = House(
            address="wrong address format!!!",
            floors=10,
            area=5,
            cost=50,
            min_time_rent=0,
            rented="yes",
        )
    except Exception as e:
        print("Validation error:", e)

    return 0


def comparing():
    house1 = House(
        address="10 green",
        floors=2,
        area=100,
        cost=1000,
        min_time_rent=6,
        rented=False,
    )

    house2 = House(
        address="20 blue",
        floors=3,
        area=100,
        cost=1200,
        min_time_rent=6,
        rented=False,
    )

    print(house1 == house2)


def main():
    scen = int(input())

    if scen == 1:
        normal()
    elif scen == 2:
        warnings_errors()
    else:
        comparing()

    return 0


if __name__ == "__main__":
    main()

import os, sys, time

from src.libs.models.commercial_house import CommercialHouse
from src.libs.models.private_house import PrivateHouse

from src.lab07.app import HouseApp
from src.lab07.exceptions import (
    HouseAppError,
    InvalidMenuChoiceError,
)
from src.lab07.color_map import (
    RESET,
    BLUE,
    CYAN,
    GREEN,
    YELLOW,
    RED,
    WHITE,
    GRAY,
    BOLD,
)


class CLI:
    def __init__(self, app: HouseApp) -> None:
        self._app = app

    def run(self) -> None:
        self._clear_screen()

        self._loading_animation("Loading data")
        self._app.load_data()

        while True:
            self._render()

            try:
                choice = input(f"{CYAN}Select option: {RESET}").strip()
                self._clear_screen()

                if choice == "0":
                    self._exit()
                    break

                menu_mapping = {
                    "1": self._add_house,
                    "2": self._show_all,
                    "3": self._find_house,
                    "4": self._filter_houses,
                    "5": self._sort_houses,
                    "6": self._remove_house,
                    "7": self._make_contract,
                    "8": self._reset_house,
                }

                if choice not in menu_mapping:
                    raise InvalidMenuChoiceError(choice)

                menu_mapping[choice]()

            except HouseAppError as error:
                self._error_message(str(error))

            except ValueError:
                self._error_message("Invalid input type")

            except Exception as error:
                self._error_message(str(error))

    def _clear_screen(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def _render(self) -> None:
        self._clear_screen()
        self._print_banner()
        self._print_stats()
        self._print_menu()

    def _print_banner(self) -> None:
        banner = rf"""{BOLD}{RED}{"=" * 70 }{RESET}
{BLUE}||{'-' * 66}||
||{' ' * 66}||
||  ██████╗  ██████╗ ██████╗       ██╗      █████╗ ██████╗ ███████╗ ||
|| ██╔═══██╗██╔═══██╗██╔══██╗      ██║     ██╔══██╗██╔══██╗██╔════╝ ||
|| ██║   ██║██║   ██║██████╔╝█████╗██║     ███████║██████╔╝███████╗ ||
|| ██║   ██║██║   ██║██╔═══╝ ╚════╝██║     ██╔══██║██╔══██╗╚════██║ ||
|| ╚██████╔╝╚██████╔╝██║           ███████╗██║  ██║██████╔╝███████║ ||
||  ╚═════╝  ╚═════╝ ╚═╝           ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ||
||{' ' * 66}||
||{'-' * 66}||
||{WHITE} Developer: {CYAN}vanil-1{' ' * 37}{RESET}{WHITE}Ver.1.0.7.{RESET}{BLUE}||
||{WHITE} Teacher: {CYAN}wilhemiv{' ' * 38}{RESET}{WHITE}19.05.2026{RESET}{BLUE}||{RESET}
{BOLD}{RED}{"=" * 70 }{RESET}"""

        print(banner)
        print(f"{WHITE}Completed labs:{RESET}")
        print(f"{GREEN}Lab01  Lab02  Lab03  Lab04  Lab05  Lab06  Lab07{RESET}")
        print(f"{GRAY}{"=" * 47}{RESET}")

    def _print_stats(self) -> None:
        houses = self._app.get_all_houses()

        private_count = sum(isinstance(h, PrivateHouse) for h in houses)
        commercial_count = sum(isinstance(h, CommercialHouse) for h in houses)
        rented_count = sum(h.rented for h in houses)
        available_count = len(houses) - rented_count

        print(f"{CYAN}District status{RESET}")
        print("-" * 20)
        print(f"Total houses: {len(houses)}")
        print(f"Private houses: {private_count}")
        print(f"Commercial houses: {commercial_count}")
        print(f"Rented: {rented_count}")
        print(f"Available: {available_count}")
        print("-" * 20)
        print()

    def _print_menu(self) -> None:
        print(f"{BOLD}{BLUE}======= HOUSE DISTRICT ======={RESET}")
        print("1. Add house")
        print("2. Show all houses")
        print("3. Find house")
        print("4. Filter houses")
        print("5. Sort houses")
        print("6. Remove house")
        print("7. Make contract")
        print("8. Reset house")
        print("0. Exit")
        print(f"{BLUE}=============================={RESET}")

    def _loading_animation(self, text: str) -> None:
        print(f"{YELLOW}{text}", end="")

        for _ in range(3):
            time.sleep(0.25)
            print(".", end="")
            sys.stdout.flush()

        print(RESET)
        time.sleep(0.2)

    def _success_message(self, message: str) -> None:
        print(f"\n{GREEN}{message}{RESET}")
        input("\nPress Enter to continue...")

    def _warning_message(self, message: str) -> None:
        print(f"\n{YELLOW}! {message}{RESET}")
        input("\nPress Enter to continue...")

    def _error_message(self, message: str) -> None:
        print(f"\n{RED}{message}{RESET}")
        input("\nPress Enter to continue...")

    def _add_house(self) -> None:
        print("\nSelect house type:")
        print("1. Private house")
        print("2. Commercial house")

        house_type = input("Type: ").strip()
        address = input("Address: ").strip()
        floors = int(input("Floors: "))
        area = float(input("Area: "))
        cost = float(input("Cost per month: "))
        min_time_rent = int(input("Min rent time(months): "))
        rented = input("Rented (y/n): ").strip().lower() == "y"

        if house_type == "1":
            mapping = {"1": "gas", "2": "electric", "3": "stove"}

            land_area = float(input("Land area: "))
            occupants_count = int(input("Occupants count: "))

            print("Heating type:")
            print("1. Gas")
            print("2. Electric")
            print("3. Stove")

            choice = input("Type:")

            if choice not in mapping:
                raise InvalidMenuChoiceError(choice)

            heating_type = mapping[choice]

            house = PrivateHouse(
                address=address,
                floors=floors,
                area=area,
                cost=cost,
                min_time_rent=min_time_rent,
                rented=rented,
                land_area=land_area,
                heating_type=heating_type,
                occupants_count=occupants_count,
            )

        elif house_type == "2":
            mapping = {"1": "office", "2": "retail", "3": "warehouse", "4": "hotel"}

            operational_area = float(input("Operational area: "))
            customers_average_count = int(input("Average customers count: "))

            print("Usage tyoe:")
            print("1. Office")
            print("2. Retail")
            print("3. Warehouse")
            print("4. Hotel")

            choice = input("Type:")

            if choice not in mapping:
                raise InvalidMenuChoiceError(choice)

            usage_type = mapping[choice]

            house = CommercialHouse(
                address=address,
                floors=floors,
                area=area,
                cost=cost,
                min_time_rent=min_time_rent,
                rented=rented,
                usage_type=usage_type,
                operational_area=operational_area,
                customers_average_count=customers_average_count,
            )

        else:
            raise ValueError("Invalid house type")

        self._loading_animation("Adding house")
        self._app.add_house(house)
        self._success_message("House successfully added")

    def _show_all(self) -> None:
        houses = self._app.get_all_houses()
        print()

        if not houses:
            self._warning_message("No houses found")

            return

        print(self._app.show_all())

        input("\nPress Enter to continue...")

    def _find_house(self) -> None:
        mapping = {"1": "address", "2": "floors", "3": "cost", "4": "area"}

        print("Field:")
        print("1. Address")
        print("2. Floors")
        print("3. Cost")
        print("4. Area")
        choice = input("Field: ")

        if choice not in mapping:
            raise InvalidMenuChoiceError(choice)

        field = mapping[choice]

        if field == "address":
            value = input("Value: ")
        elif field in ("cost", "area"):
            value = float(input("Value: "))
        else:
            value = int(input("Value: "))

        result = self._app.find_houses(field, value)
        print()

        if not result:
            self._warning_message("Nothing found")

            return

        print(self._app.list_to_table(result))

        input("\nPress Enter to continue...")

    def _filter_houses(self) -> None:
        print("\nFilter options:")
        print("1. Not rented")
        print("2. Cost > X")
        print("3. Area > X")

        choice = input("Select: ")

        if choice == "1":
            result = self._app.filter_houses("1", 0)

        elif choice == "2":
            x = float(input("Min cost: "))
            result = self._app.filter_houses("2", x)

        elif choice == "3":
            x = float(input("Min area: "))
            result = self._app.filter_houses("3", x)

        else:
            raise InvalidMenuChoiceError(choice)

        print()

        print(self._app.list_to_table(result))

        input("\nPress Enter to continue...")

    def _sort_houses(self) -> None:
        mapping = {"1": "address", "2": "cost", "3": "area", "4": "floors"}

        print("\nSort by:")
        print("1. Address")
        print("2. Cost")
        print("3. Area")
        print("4. Floors")

        choice = input("Select: ")

        if choice not in mapping:
            raise InvalidMenuChoiceError(choice)

        result = self._app.sort_houses(mapping[choice])

        print()

        print(self._app.list_to_table(result))

        input("\nPress Enter to continue...")

    def _remove_house(self) -> None:
        address = input("Enter address to remove: ")
        confirm = input(f"Delete '{address}'? (y/n): ")

        if confirm.lower() != "y":
            self._warning_message("Operation cancelled")

            return

        self._app.remove_house(address)
        self._success_message("Removed successfully")

    def _make_contract(self) -> None:
        address = input("Enter address: ")

        self._app.make_contract(address)
        self._success_message("Contract created")

    def _reset_house(self) -> None:
        address = input("Enter address: ")

        self._app.reset_house(address)
        self._success_message("House reset")

    def _exit(self) -> None:
        confirm = input("Save changes? (y/n): ")
        if confirm.lower() != "y":
            print(f"{YELLOW}Changes aren't saved!{RESET}")

            return

        self._loading_animation("Saving data")
        self._app.save_data()

        print(f"\n{GREEN}Complete!{RESET}")

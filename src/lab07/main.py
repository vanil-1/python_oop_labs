from src.lab07.app import HouseApp
from src.lab07.cli import CLI


def main() -> None:
    storage_path = "data/lab07/data.json"
    district_name = "Default District"

    app = HouseApp(
        district_name=district_name,
        storage_path=storage_path,
    )

    cli = CLI(app)
    cli.run()


if __name__ == "__main__":
    main()

class HouseAppError(Exception):
    """Base exception for the House District application."""

    def __init__(self, message: str = "Application error.") -> None:
        super().__init__(message)


class HouseNotFoundError(HouseAppError):
    def __init__(self, address: str) -> None:
        message = f"House with address '{address}' was not found."
        super().__init__(message)


class DuplicateHouseError(HouseAppError):
    def __init__(self, address: str) -> None:
        message = f"House with address '{address}' already exists."
        super().__init__(message)


class InvalidMenuChoiceError(HouseAppError):
    def __init__(self, choice: str) -> None:
        message = f"Invalid menu choice: '{choice}'."
        super().__init__(message)


class EmptyDistrictError(HouseAppError):
    def __init__(self) -> None:
        message = "District contains no houses."
        super().__init__(message)


class StorageError(HouseAppError):
    def __init__(self, operation: str, filepath: str) -> None:
        message = (
            f"Storage error during '{operation}' " f"operation for file '{filepath}'."
        )
        super().__init__(message)

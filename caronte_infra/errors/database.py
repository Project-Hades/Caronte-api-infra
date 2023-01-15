class UndefinedDatabaseException(Exception):
    def __init__(self, error: str) -> None:
        super().__init__("Undefined database.")
        self.error = error

    def __str__(self) -> str:
        return f"{super().__str__()} {self.error}"


class UndefinedFieldConfiguration(Exception):
    def __init__(self, error: str) -> None:
        super().__init__("Undefined field configuration.")
        self.error = error

    def __str__(self) -> str:
        return f"{super().__str__()} {self.error}"

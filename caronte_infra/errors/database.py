class UndefinedDatabaseException(Exception):
    def __init__(self, error: str) -> None:
        super().__init__(f"Undefined database. {error}")


class UndefinedFieldConfiguration(Exception):
    def __init__(self, error: str) -> None:
        super().__init__(f"Undefined field configuration. {error}")

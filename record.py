class Record:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"

    def __repr__(self) -> str:
        return f"Record({self.name}, {self.number})"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Record):
            return self.name == o.name and self.number == o.number
        return super().__eq__(o)

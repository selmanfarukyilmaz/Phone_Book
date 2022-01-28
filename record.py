from linked_list import DoublyLinkedList


class Person:

    def __init__(self, name: str, numbers: DoublyLinkedList):
        self.name = name
        self.numbers = numbers

    def __str__(self) -> str:
        return f"{self.name} --> {self.numbers}"

    def __repr__(self) -> str:
        return f"Record({self.name}, {self.numbers})"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Person):
            return self.name == o.name and self.numbers == o.numbers
        return super().__eq__(o)


class PhoneRecord:

    def __init__(self, number_type: str, number: str):
        self.number_type = number_type
        self.number = number

    def __str__(self) -> str:
        return f"{self.number_type}: {self.number}"

    def __repr__(self) -> str:
        return f"Record({self.number_type}, {self.number})"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, PhoneRecord):
            return self.number_type == o.number_type and self.number == o.number
        return super().__eq__(o)

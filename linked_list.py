from typing import Optional


class DoublyNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f"{self.data}"


class DoublyLinkedList:

    def __init__(self):
        self.head: Optional[DoublyNode] = None

    def __str__(self) -> str:
        return f"{self.head}"


    def add(self, new_node: DoublyNode):
        if not self.head:
            self.head = new_node
            return

        # find last node
        last = self.head
        while last.next:
            last = last.next
        # insert
        last.next = new_node
        new_node.prev = last

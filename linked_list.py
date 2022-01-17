from typing import Optional


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None

    def show(self):
        """
        Print nodes of the linked list to the screen
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def add(self, new_node: Node):
        if not self.head:
            self.head = new_node
            return

        # find last node
        last = self.head
        while last.next:
            last = last.next
        # insert
        last.next = new_node

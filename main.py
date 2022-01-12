from linked_list import LinkedList, Node
from record import Record

if __name__ == '__main__':
    r1 = Record(name="selman", number="541")
    r2 = Record(name="mustafa", number="542")
    r3 = Record(name="fatih", number="543")
    r1_node = Node(data=r1)
    r2_node = Node(data=r2)
    r3_node = Node(data=r3)
    phone_book = LinkedList()
    phone_book.head = r1_node
    r1_node.next = r2_node
    r2_node.next = r3_node

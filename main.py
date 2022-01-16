from linked_list import LinkedList, Node
from record import Record


def add_record(linked_list: LinkedList, name: str, number: str):
    new_record = Record(name=name, number=number)
    new_node = Node(data=new_record)
    linked_list.add(new_node)


if __name__ == '__main__':
    r1 = Record(name="selman", number="541")
    r2 = Record(name="mustafa", number="542")
    r1_node = Node(data=r1)
    r2_node = Node(data=r2)
    phone_book = LinkedList()
    phone_book.head = r1_node
    r1_node.next = r2_node

    add_record(linked_list=phone_book, name="fatih", number="543")
    add_record(linked_list=phone_book, name="kadir", number="544")
    phone_book.show()


    def remove(name):
        temp = phone_book.head

        if temp.data.name == name:
            phone_book.head = temp.next
            temp = None
            return

        while temp:
            if temp.data.name == name:
                before.next = temp.next
                temp = None
                break
            before = temp
            temp = temp.next

        if temp is None:
            return


    def update(name,new_name,new_number):
        temp = phone_book.head
        while temp:
            if temp.data.name == name:
                temp.data.number = new_number
                temp.data.name = new_name
                break
            temp = temp.next

        if temp is None:
            return


    def search(name):
        temp = phone_book.head
        len_search = len(name)
        while temp:
            if temp.data.name[:len_search] == name:
                print(f"Name: {temp.data.name} --> Number: {temp.data.number}")
            temp = temp.next


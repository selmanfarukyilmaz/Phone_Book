from linked_list import LinkedList, Node
from record import Record


def add_record(linked_list: LinkedList, name: str, number: str):
    new_record = Record(name=name, number=number)
    new_node = Node(data=new_record)
    linked_list.add(new_node)


def remove_record(linked_list: LinkedList, name: str):
    if linked_list.head.data.name == name:
        linked_list.head = linked_list.head.next
        return

    prev = phone_book.head
    # find the previous node
    while prev.next and prev.next.data.name != name:
        prev = prev.next

    if prev.next:
        prev.next = prev.next.next
    else:
        print("not found")


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
    remove_record(linked_list=phone_book, name="mustafa")
    remove_record(linked_list=phone_book, name="kadir")
    remove_record(linked_list=phone_book, name="selman")



    def update(name, new_name, new_number):
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


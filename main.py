from linked_list import LinkedList, Node
from record import Record


def add_record():
    """
    Allows adding a new user to the phone book.
    The name and number information of the person to be added to the phone book is obtained from the user.

    """
    print("Please enter the name of the person you want to add to the phone book: ")
    name = str(input())
    print("Please enter the number of the person you want to add to the phone book: ")
    number = str(input())
    print(f"{name}: {number} successfully added to your phone book.")
    new_record = Record(name=name, number=number)
    new_node = Node(data=new_record)
    phone_book.add(new_node)


def remove_record():
    """
    Deletes the user registered in the phone book.
    It asks the user for the name of the user registered in the phone book and then deletes it.

    """
    print("Please enter the name of the person you want to delete from the phone book: ")
    name = str(input())
    if phone_book.head.data.name == name:
        phone_book.head = phone_book.head.next
        print(f"{name} has been successfully deleted from the phone book.")
        return

    prev = phone_book.head
    # find the previous node
    while prev.next and prev.next.data.name != name:
        prev = prev.next

    if prev.next:
        prev.next = prev.next.next
        print(f"{name} has been successfully deleted from the phone book.")
    else:
        print("not found")


def search_prefix():
    """
    Searches the phone book by reference to the name.
    The results starting with the input entered by the user are printed on the screen.

    """
    print("Enter the name you want to search in the phone book: ")
    prefix = str(input())
    temp = phone_book.head
    while temp:
        if temp.data.name.startswith(prefix):
            print(temp.data)
        temp = temp.next


def update():
    """
    Updates the name or number of a contact in the phone book.
    """
    temp = phone_book.head
    print("Please enter the registered name whose information you want to update: ")
    input_name = str(input())
    print(f"Enter the new name of {input_name} you want to update: (Press enter for no change)")
    input_new_name = str(input())
    print(f"Enter the new number of {input_name} you want to update: (Press enter for no change)")
    input_new_number = str(input())

    if input_new_name == "" and input_new_number == "":
        print("No changes have been made.")
        return

    if input_new_name != "" and input_new_number == "":
        print(f"{input_name} name was changed to {input_new_name}.")
        while temp:
            if temp.data.name == input_name:
                temp.data.name = input_new_name
                break
            temp = temp.next

    if input_new_name == "" and input_new_number != "":
        print(f"{input_new_name}'s number has been changed to {input_new_number}.")
        while temp:
            if temp.data.name == input_name:
                temp.data.number = input_new_number
                break
            temp = temp.next

    if input_new_name != "" and input_new_number != "":
        print(f"{input_name} name has been updated to {input_new_name} and The phone number has been updated to {input_new_number}.")
        while temp:
            if temp.data.name == input_name:
                temp.data.number = input_new_number
                temp.data.name = input_new_name
                break
            temp = temp.next

    if temp is None:
        return



if __name__ == '__main__':
    r1 = Record(name="selman", number="541")
    r2 = Record(name="mustafa", number="542")
    r1_node = Node(data=r1)
    r2_node = Node(data=r2)
    phone_book = LinkedList()
    phone_book.head = r1_node
    r1_node.next = r2_node

    while True:
        print("Please enter the number next to the operation you want to do.")
        print("1- View contacts in the phone book.\n2- Add a new contact to the phone book."
              "\n3- Delete a contact in the phone book.\n4- Update the information of a contact in the phone book."
              "\n5- Searching the phone book by name.\n6- Exit")
        action = str(input())
        if action == "1":
            phone_book.show()
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break
        if action == "2":
            add_record()
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break
        if action == "3":
            remove_record()
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break
        if action == "4":
            update()
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break
        if action == "5":
            search_prefix()
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break
        if action == "6":
                break
        else:
            print("Please press 1,2,3,4,5 or 6 according to the operation you want to do.")




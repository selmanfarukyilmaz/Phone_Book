from linked_list import LinkedList, Node
from record import Record


def add_record(linked_list: LinkedList):
    """
    Allows adding a new user to the phone book.
    The name and number information of the person to be added to the phone book is obtained from the user.

    """
    print("Please enter the name of the person you want to add to the phone book: ")
    name = str(input()).title()

    print("Please enter the number of the person you want to add to the phone book: ")
    number = str(input())

    print(f"{name}: {number} successfully added to your phone book.")

    new_record = Record(name=name, number=number)
    new_node = Node(data=new_record)
    linked_list.add(new_node)


def remove_record(linked_list: LinkedList):
    """
    Deletes the user registered in the phone book.
    It asks the user for the name of the user registered in the phone book and then deletes it.

    """
    print("Please enter the name of the person you want to delete from the phone book: ")
    name = str(input()).title()

    if linked_list.head.data.name == name:
        linked_list.head = linked_list.head.next
        print(f"{name} has been successfully deleted from the phone book.")
        return

    prev = linked_list.head
    # find the previous node
    while prev.next and prev.next.data.name != name:
        prev = prev.next

    if prev.next:
        prev.next = prev.next.next
        print(f"{name} has been successfully deleted from the phone book.")
    else:
        print(f"{name} name not found in phone book")


def search_prefix(linked_list: LinkedList):
    """
    Searches the phone book by reference to the name.
    The results starting with the input entered by the user are printed on the screen.

    """
    print("Enter the name you want to search in the phone book: ")
    prefix = str(input()).title()
    temp = linked_list.head
    count = 0
    while temp:
        if temp.data.name.startswith(prefix):
            count += 1
            print(temp.data)
        temp = temp.next
    if count == 0:
        print("No one with the name you are looking for was found in the phone book.")


def update(linked_list: LinkedList):
    """
    Updates the name or number of a contact in the phone book.
    """
    temp = linked_list.head
    print("Please enter the registered name whose information you want to update: ")
    input_name = str(input()).title()
    check = False
    while temp:
        if temp.data.name == input_name:
            check = True
            break
        temp = temp.next

    if check is not True:
        print(f"{input_name} name not found in phone book")
        return

    print(f"Enter the new name of {input_name} you want to update: (Press enter for no change)")
    input_new_name = str(input()).title()

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
        print(f"{input_name}'s number has been changed to {input_new_number}.")
        while temp:
            if temp.data.name == input_name:
                temp.data.number = input_new_number
                break
            temp = temp.next

    if input_new_name != "" and input_new_number != "":
        print(
            f"{input_name} name has been updated to {input_new_name} and "
            f"The phone number has been updated to {input_new_number}.")
        while temp:
            if temp.data.name == input_name:
                temp.data.number = input_new_number
                temp.data.name = input_new_name
                break
            temp = temp.next

    if temp is None:
        return

from linked_list import LinkedList, Node
from record import Record
from termcolor import colored
import os.path


def add_record(linked_list: LinkedList):
    """
    Allows adding a new user to the phone book.
    The name and number information of the person to be added to the phone book is obtained from the user.

    """
    print("Please enter the name of the person you want to add to the phone book: ")
    name = str(input()).title()
    if not name:
        print("You did not enter a valid name")
        return
    print("Please enter the number of the person you want to add to the phone book: ")
    number = str(input())
    if not number:
        print("You did not enter a valid number")
        return

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

    if input_new_name:
        temp.data.name = input_new_name
    if input_new_number:
        temp.data.number = input_new_number
    print(f"{temp.data.name}: {temp.data.number}")

    if temp is None:
        return


def interface(linked_list: LinkedList):
    if os.path.isfile("phonebook.txt"):
        text_file = open("phonebook.txt", "r")
        data = text_file.read()
        text_file.close()
        data = data.split("*+-")

        name_temp = []
        number_temp = []
        for i, datas in enumerate(data):
            if i % 2 == 0:
                name_temp.append(datas)
            else:
                number_temp.append(datas)

        for name, number in zip(name_temp, number_temp):
            new_record = Record(name=name, number=number)
            new_node = Node(data=new_record)
            linked_list.add(new_node)

    print(colored(">>>>>>>>Welcome to Phone Book<<<<<<<<", "yellow", attrs=['bold']))
    while True:
        print(colored("↓ Select the Action you want to use ↓", "green", attrs=['bold']))
        print(colored("1- View contacts in the phone book.\n"
                      "2- Add a new contact to the phone book.\n"
                      "3- Delete a contact in the phone book.\n"
                      "4- Update the information of a contact in the phone book.\n"
                      "5- Searching the phone book by name.\n"
                      "6- Exit", attrs=['bold']))

        action = str(input())

        if action == "1":
            linked_list.show()
            print("Press any key to continue")
            input()
            continue

        if action == "2":
            add_record(linked_list)
            print("Press any key to continue")
            input()
            continue

        if action == "3":
            remove_record(linked_list)
            print("Press any key to continue")
            input()
            continue

        if action == "4":
            update(linked_list)
            print("Press any key to continue")
            input()
            continue

        if action == "5":
            search_prefix(linked_list)
            print("Press any key to continue")
            input()
            continue

        if action == "6":
            temp = linked_list.head
            f = open("phonebook.txt", "w")
            while temp:
                name_str = str(temp.data.name + "*+-")
                f.write(name_str)
                number_str = str(temp.data.number + "*+-")
                f.write(number_str)
                temp = temp.next

            f.close()
            break

        else:
            print("Please press 1,2,3,4,5 or 6 according to the operation you want to do.")
            print("Press any key to continue")
            input()

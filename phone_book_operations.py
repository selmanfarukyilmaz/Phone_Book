import os.path
import time

from termcolor import colored

from linked_list import LinkedList, Node
from record import Record


def add_record(linked_list: LinkedList):
    """
    Allows adding a new user to the phone book.
    The name and number information of the person to be added to the phone book is obtained from the user.

    """
    name = str(input("Please enter the name of the person you want to add to the phone book: "))
    if not name:
        print("You did not enter a valid name")
        return
    number = str(input("Please enter the number of the person you want to add to the phone book: "))
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
    name = str(input("Please enter the name of the person you want to delete from the phone book: "))

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
    prefix = str(input("Enter the name you want to search in the phone book: "))
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
    input_name = str(input("Please enter the registered name whose information you want to update: "))
    check = False
    while temp:
        if temp.data.name == input_name:
            check = True
            break
        temp = temp.next

    if check is not True:
        print(f"{input_name} name not found in phone book")
        return

    input_new_name = str(input(f"Enter the new name of {input_name} you want to update: (Press enter for no change)"))

    input_new_number = str(
        input(f"Enter the new number of {input_name} you want to update: (Press enter for no change)"))

    temp.data.name = input_new_name or temp.data.name
    temp.data.number = input_new_number or temp.data.number
    print(f"{temp.data.name}: {temp.data.number}")


def reset(linked_list: LinkedList):
    """
    It deletes all data and creates a new phone book.
    """
    variable = input("This operation will delete all record information in the phone book. Press \"1\" to perform the "
                     "reset.\nPress any key to cancel")
    if variable == 1:
        linked_list.head = None


def load_records(linked_list: LinkedList):
    global delimiter_line
    global delimiter_word
    global txt_name
    txt_name = "phonebook.txt"
    delimiter_line = "\n"
    delimiter_word = ","

    if os.path.isfile(txt_name):
        txt_name = txt_name
        with open(file=txt_name, mode="r") as file:
            records = file.read()
            records = records.split(delimiter_line)
            for r in records[:-1]:
                name, number = r.split(delimiter_word)
                new_record = Record(name=name, number=number)
                new_node = Node(data=new_record)
                linked_list.add(new_node)


def save(linked_list: LinkedList):
    temp = linked_list.head
    with open(file=txt_name, mode="w") as file:
        while temp:
            file.write(f"{temp.data.name}{delimiter_word}{temp.data.number}{delimiter_line}")
            temp = temp.next


def menu():
    print(colored("↓ Select the Action you want to use ↓", "green", attrs=['bold']))
    print(colored("1- View contacts in the phone book.\n"
                  "2- Add a new contact to the phone book.\n"
                  "3- Delete a contact in the phone book.\n"
                  "4- Update the information of a contact in the phone book.\n"
                  "5- Searching the phone book by name.\n"
                  "6- Reset phone book.\n"
                  "7- Exit", attrs=['bold']))


def help_me():
    print("Please press 1,2,3,4,5 or 6 according to the operation you want to do.")
    time.sleep(2)
    input("Press any key to continue")


def interface(linked_list: LinkedList):
    print(colored(">>>>>>>>Welcome to Phone Book<<<<<<<<", "yellow", attrs=['bold']))

    load_records(linked_list)
    action = 0
    while action != "7":

        menu()
        action = str(input())

        if action == "1":
            linked_list.show()
            input("Press any key to continue")

        elif action == "2":
            add_record(linked_list)
            input("Press any key to continue")

        elif action == "3":
            remove_record(linked_list)
            input("Press any key to continue")

        elif action == "4":
            update(linked_list)
            input("Press any key to continue")

        elif action == "5":
            search_prefix(linked_list)
            input("Press any key to continue")

        elif action == "6":
            reset(linked_list)

        elif action == "7":
            save(linked_list)

        else:
            help_me()

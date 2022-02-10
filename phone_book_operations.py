import configparser
import os.path
import time
from termcolor import colored

from linked_list import DoublyLinkedList, DoublyNode
from record import Person, PhoneRecord


CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")
PHONEBOOK_FILE_NAME = CONFIG["DEFAULT"]["phonebook_file_name"]
DELIMITER_LINE = "\n"
DELIMITER_WORD = CONFIG["DEFAULT"]["delimiter_word"]
DELIMITER_NUMBER = CONFIG["DEFAULT"]["delimiter_number"]
DELIMITER_RECORD = CONFIG["DEFAULT"]["delimiter_record"]


def name_search(linked_list: DoublyLinkedList, name):
    temp = linked_list.head
    while temp:
        if temp.data.name == name:
            return temp
        temp = temp.next

    print("The name you entered was not found in the phone book")
    return


def add_person(linked_list: DoublyLinkedList):
    """
    Allows adding a new user to the phone book.
    The name and number information of the person to be added to the phone book is obtained from the user.

    """
    name = str(input("Please enter the name of the person you want to add to the phone book: "))
    if not name:
        print("You did not enter a valid name")
        return

    print(f"{name} successfully added to your phone book.")

    new_record = Person(name=name, numbers=DoublyLinkedList())
    new_node = DoublyNode(data=new_record)
    linked_list.add(new_node)


def add_number(linked_list: DoublyLinkedList):
    name = str(input("Please enter the name you want to enter the number and phone type."))
    temp = name_search(linked_list, name)
    if not temp:
        return

    number = str(input(f"Please enter the number you want to add to {name}."))
    if not number:
        print("You did not enter a valid number.")
        return
    number_type = str(input(f"Please enter the type of phone number {number} that you added to {name}"))
    if not number_type:
        print("You did not enter a valid number type.")
        return
    new_record = PhoneRecord(number=number, number_type=number_type)
    new_node = DoublyNode(data=new_record)
    temp.data.numbers.add(new_node)


def remove_person(linked_list: DoublyLinkedList):
    """
    Deletes the user registered in the phone book.
    It asks the user for the name of the user registered in the phone book and then deletes it.

    """
    # Error prevention if Number = None.
    try:
        if linked_list.head.data:
            pass
    except:
        print("There is no number to delete.")
        return

    name = str(input("Please enter the name of the person you want to delete from the phone book: "))

    if linked_list.head.data.name == name:
        linked_list.head = linked_list.head.next
        print(f"{name} has been successfully deleted from the phone book.")
        return

    curr = linked_list.head
    # find the curr node
    while curr.next and curr.next.data.name != name:
        curr = curr.next
    # try:
    if curr.next:
        curr.next = curr.next.next
        print(f"{name} has been successfully deleted from the phone book.")
        return

    else:
        print(f"{name} name not found in phone book")


def remove_number(linked_list: DoublyLinkedList):
    name = str(input("Please Enter the name whose number you want to delete: "))
    temp = name_search(linked_list, name)
    if not temp:
        return

    previous = temp.data.numbers
    temp = temp.data.numbers.head

    # Error prevention if Number = None.
    try:
        if previous.head.data:
            pass
    except:
        print("There is no number to delete.")
        return

    # print numbers and number types
    while temp:
        print(f"{temp.data.number_type}: {temp.data.number}")
        temp = temp.next

    number = input(str("Enter the number you want to delete: "))
    # find the previous node

    # if head == number solution
    if previous.head.data.number == number:
        previous.head = previous.head.next
        return

    # if head.next == number solution
    previous = previous.head
    while previous.next:
        if previous.next.data.number == number:
            previous.next = previous.next.next
            return
        previous = previous.next

    else:
        print("There is no number to delete.")


def update_person(linked_list: DoublyLinkedList):
    """
     Updates the name of a contact in the phone book.
     """
    # temp = linked_list.head
    name = str(input("Please enter the registered name whose information you want to update: "))
    temp = name_search(linked_list, name)
    if not temp:
        return

    input_new_name = str(input(f"Enter the new name of {name} you want to update: "))

    temp.data.name = input_new_name

    print(f"{temp.data.name} Updated !")


def update_number(linked_list: DoublyLinkedList):
    """
     Updates the name of a contact in the phone book.
     """
    # temp = linked_list.head
    name = str(input("Please enter the registered name whose information you want to update: "))
    temp = name_search(linked_list, name)
    if not temp:
        return

    curr = temp.data.numbers.head
    temp = temp.data.numbers.head

    while temp:
        print(f"{temp.data.number_type}: {temp.data.number}")
        temp = temp.next

    number = str(input("Enter the number you want to update: "))
    new_number = str(input("Enter the new number: "))

    while curr:
        if curr.data.number == number:
            curr.data.number = new_number
            return
        curr = curr.next
    else:
        print(f"The {number} you entered is not in the records of {name}.")


def search_prefix(linked_list: DoublyLinkedList):
    """
    Searches the phone book by reference to the name.
    The results starting with the input entered by the user are printed on the screen.

    """
    prefix = str(input("Enter the name you want to search in the phone book: "))
    temp = linked_list.head
    variable = False
    while temp:
        if temp.data.name.startswith(prefix):
            variable = True
            print(temp.data.name)
            curr = temp.data.numbers.head
            try:
                while curr.data.number:
                    print(f"{curr.data.number} --> {curr.data.number_type}")
                    curr = curr.next
            except:
                pass

        temp = temp.next
    if not variable:
        print("No one with the name you are looking for was found in the phone book.")


def show(linked_list: DoublyLinkedList):
    temp = linked_list.head
    while temp:
        if temp.data.name:
            print(temp.data.name)
            try:
                curr = temp.data.numbers.head
                while curr.data.number:
                    print(f"{curr.data.number} --> {curr.data.number_type}")
                    curr = curr.next
            except:
                pass

        temp = temp.next


def load_records(linked_list: DoublyLinkedList):
    if os.path.isfile(PHONEBOOK_FILE_NAME):
        with open(file=PHONEBOOK_FILE_NAME, mode="r") as file:
            records = file.read()
            records = records.split(DELIMITER_LINE)
            for r in records[1:]:
                name, numbers = r.split(DELIMITER_WORD)
                new_record = Person(name=name, numbers=DoublyLinkedList())
                new_node = DoublyNode(data=new_record)

                if numbers:
                    numbers = numbers[:-1]
                    for n in numbers.split(DELIMITER_RECORD):
                        number, number_type = n.split(DELIMITER_NUMBER)
                        new_record = PhoneRecord(number=number, number_type=number_type)
                        new_node_number = DoublyNode(data=new_record)
                        new_node.data.numbers.add(new_node_number)

                linked_list.add(new_node)


def save(linked_list: DoublyLinkedList):
    temp = linked_list.head
    with open(file="phonebook.txt", mode="w") as file:
        while temp:
            file.write(f"{DELIMITER_LINE}{temp.data.name}{DELIMITER_WORD}")

            curr = temp.data.numbers.head
            while curr:
                file.write(f"{curr.data.number}{DELIMITER_NUMBER}{curr.data.number_type}{DELIMITER_RECORD}")
                curr = curr.next

            temp = temp.next


def menu():
    print(colored("↓ Select the Action you want to use ↓", "green", attrs=['bold']))
    print(colored("1- View contacts in the phone book.\n"
                  "2- Add a new contact to the phone book.\n"
                  "3- Add number to contact\n"
                  "4- Delete a contact in the phone book.\n"
                  "5- Delete a contact's number\n"
                  "6- Update the name of a contact in the phone book.\n"
                  "7- Update the number of a contact in the phone book.\n"
                  "8- Searching the phone book by name.\n"
                  "9- Exit", attrs=['bold']))


def help_me():
    print("Please press 1,2,3,4,5 or 6 according to the operation you want to do.")
    time.sleep(2)
    input("Press any key to continue")


def interface(linked_list: DoublyLinkedList):
    print(colored(">>>>>>>>Welcome to Phone Book<<<<<<<<", "yellow", attrs=['bold']))

    load_records(linked_list)

    while True:

        menu()
        action = str(input())

        if action == "1":
            show(linked_list)
            input("Press any key to continue")

        elif action == "2":
            add_person(linked_list)
            input("Press any key to continue")

        elif action == "3":
            add_number(linked_list)
            input("Press any key to continue")

        elif action == "4":
            remove_person(linked_list)
            input("Press any key to continue")

        elif action == "5":
            remove_number(linked_list)
            input("Press any key to continue")

        elif action == "6":
            update_person(linked_list)
            input("Press any key to continue")
        elif action == "7":
            update_number(linked_list)
            input("Press any key to continue")
        elif action == "8":
            search_prefix(linked_list)
            input("Press any key to continue")
        elif action == "9":
            save(linked_list)
            return
        else:
            help_me()

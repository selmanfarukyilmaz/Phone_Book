import configparser
import os.path
import time
from typing import Optional

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


def search_person_node_by_name(linked_list: DoublyLinkedList, name: str) -> Optional[DoublyNode]:
    """
    Search name in given linked list, and return node.
    Nodes of the linked list must be Person instances.

    :param linked_list: linked list Person instances
    :type linked_list: DoublyLinkedList
    :param name: name to be searched
    :type name: str
    :return: node found in the list
    :rtype: Optional[DoublyNode]
    """
    curr = linked_list.head
    while curr:
        if curr.data.name == name:
            return curr
        curr = curr.next
    print("The name you entered was not found in the phone book")


def search_phone_record_node_by_number(
        numbers: DoublyLinkedList,
        number: str,
) -> Optional[DoublyNode]:
    curr = numbers.head
    while curr:
        if curr.data.number == number:
            return curr
        curr = curr.next
    print("The number you entered was not found in the phone book")


def add_person(linked_list: DoublyLinkedList):
    """
    Add a new user to the phone book. The name and number information of the
    person to be added to the phone book is obtained from the user.
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
    name = str(input("Please enter the name of existing person: "))
    found_record = search_person_node_by_name(linked_list, name)
    if not found_record:
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
    found_record.data.numbers.add(new_node)


def remove_person(linked_list: DoublyLinkedList):
    """
    Delete the user registered in the phone book.
    It asks the user for the name of the user registered in the phone book and then deletes it.

    """
    # empty linked list, so there is no person to delete
    if not linked_list.head:
        print("There is no person to delete.")
        return

    name = str(input("Please enter the name of the person you want to delete from the phone book: "))

    # delete head, if head.name = name
    if linked_list.head.data.name == name:
        linked_list.head = linked_list.head.next
        # person count >= 2
        if linked_list.head:
            linked_list.head.prev = None
        print(f"{name} has been successfully deleted from the phone book.")
        return

    found_record = search_person_node_by_name(linked_list, name)
    if not found_record:
        print(f"{name} name not found in phone book")
    else:
        found_record.prev.next = found_record.next
        # skip if found_record is the last record in the linked list
        if found_record.next:
            found_record.next.prev = found_record.prev
        print(f"{name} has been successfully deleted from the phone book.")


def remove_number(linked_list: DoublyLinkedList):
    name = str(input("Please Enter the name whose number you want to delete: "))
    found_person = search_person_node_by_name(linked_list, name)
    if not found_person:
        return

    found_person_numbers = found_person.data.numbers
    # empty linked list, so there is no number to delete
    if not found_person_numbers.head:
        print("There is no number to delete.")
        return

    # print phone numbers of found_person with number types
    curr_phone_record = found_person_numbers.head
    while curr_phone_record:
        print(f"{curr_phone_record.data.number_type}: {curr_phone_record.data.number}")
        curr_phone_record = curr_phone_record.next

    number = input(str("Enter the number you want to delete: "))
    # find the number node to be deleted
    phone_to_delete = search_phone_record_node_by_number(found_person_numbers, number)

    # if first number, fix head
    if not phone_to_delete.prev:
        found_person_numbers.head = phone_to_delete.next
    else:
        phone_to_delete.prev.next = phone_to_delete.next
    # skip if last number
    # if not last number, fix next number's prev
    if phone_to_delete.next:
        phone_to_delete.next.prev = phone_to_delete.prev


def update_person(linked_list: DoublyLinkedList):
    """
     Updates the name of a contact in the phone book.
     """
    name = str(input("Please enter the registered name whose information you want to update: "))
    temp = search_person_node_by_name(linked_list, name)
    if not temp:
        return

    input_new_name = str(input(f"Enter the new name of {name} you want to update: "))
    temp.data.name = input_new_name
    print(f"{temp.data.name} Updated !")


def update_number(linked_list: DoublyLinkedList):
    """
     Updates the name of a contact in the phone book.
     """
    name = str(input("Please enter the registered name whose information you want to update: "))
    temp = search_person_node_by_name(linked_list, name)
    if not temp:
        return

    # print phone numbers of found_person with number types
    curr_phone_record = temp.data.numbers.head
    while curr_phone_record:
        print(f"{curr_phone_record.data.number_type}: {curr_phone_record.data.number}")
        curr_phone_record = curr_phone_record.next

    number = str(input("Enter the number you want to update: "))

    phone_record = search_phone_record_node_by_number(temp.data.numbers, number)
    if not phone_record:
        print(f"The {number} you entered is not in the records of {name}.")
    else:
        new_number = str(input("Enter the new number: "))
        phone_record.data.number = new_number
        print(f"{phone_record.data.number_type} Updated !")


def search_prefix(linked_list: DoublyLinkedList):
    """
    Searches the phone book by reference to the name.
    The results starting with the input entered by the user are printed on the screen.

    """
    prefix = str(input("Enter the name you want to search in the phone book: "))
    temp = linked_list.head
    prefix_match_flag = False
    while temp:
        if temp.data.name.startswith(prefix):
            prefix_match_flag = True
            print(temp.data.name)
            curr = temp.data.numbers.head
            if curr:
                while curr and curr.data.number:
                    print(curr)
                    curr = curr.next

        temp = temp.next
    if not prefix_match_flag:
        print("No one with the name you are looking for was found in the phone book.")


def show(linked_list: DoublyLinkedList):
    temp = linked_list.head
    while temp:
        if temp.data.name:
            print(temp.data.name)
            try:
                curr = temp.data.numbers.head
                while curr.data.number:
                    print(curr)
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
    with open(file=PHONEBOOK_FILE_NAME, mode="w") as file:
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

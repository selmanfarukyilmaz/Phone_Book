import os.path
import time
from termcolor import colored

from linked_list import DoublyLinkedList, DoublyNode
from record import Person, PhoneRecord


def add_name(linked_list: DoublyLinkedList):
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
    temp = linked_list.head
    valid_check = False
    while temp:
        if temp.data.name == name:
            valid_check = True
            break
        temp = temp.next

    if not valid_check:
        print("The name you entered was not found in the phone book")
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


def remove_record(linked_list: DoublyLinkedList):
    """
    Deletes the user registered in the phone book.
    It asks the user for the name of the user registered in the phone book and then deletes it.

    """
    name = str(input("Please enter the name of the person you want to delete from the phone book: "))

    if linked_list.head.data.name == name:
        linked_list.head = linked_list.head.next
        print(f"{name} has been successfully deleted from the phone book.")
        return

    previous = linked_list.head
    # find the previous node
    while previous.next and previous.next.data.name != name:
        previous = previous.next

    if previous.next:
        previous.next = previous.next.next
        previous.next.prev = previous
        print(f"{name} has been successfully deleted from the phone book.")
    else:
        print(f"{name} name not found in phone book")


def remove_number(linked_list: DoublyLinkedList):
    name = str(input("Please Enter the name whose number you want to delete: "))
    temp = linked_list.head
    valid_check = False
    while temp:
        if temp.data.name == name:
            valid_check = True
            break
        temp = temp.next

    if not valid_check:
        print("The name you entered was not found in the phone book")
        return

    previous = temp.data.numbers

    # print(previous)
    # print(type(previous))
    # print(previous.head)
    # print(previous.head.next)
    temp = temp.data.numbers.head
    while temp:
        print(temp.data.number)
        temp = temp.next

    number = input(str("Enter the number you want to delete: "))
    # find the previous node
    if previous.head.data.number == number:
        previous.head = previous.head.next
        print(30)
        return
    previous = previous.head
    while previous:
        print(40)
        if previous.next.data.number == number:
            previous.next = previous.next.next
            return
        previous = previous.next
    else:
        print("error")

phone_book = DoublyLinkedList()
phone_book.show()
remove_number(phone_book)
# remove_record(phone_book)
add_name(phone_book)
add_number(phone_book)
# def search_prefix(linked_list: DoublyLinkedList):
#     """
#     Searches the phone book by reference to the name.
#     The results starting with the input entered by the user are printed on the screen.
#
#     """
#     prefix = str(input("Enter the name you want to search in the phone book: "))
#     temp = linked_list.head
#     count = 0
#     while temp:
#         if temp.data.name.startswith(prefix):
#             count += 1
#             print(temp.data)
#         temp = temp.next
#     if count == 0:
#         print("No one with the name you are looking for was found in the phone book.")
#
#
# def update(linked_list: DoublyLinkedList):
#     """
#     Updates the name or number of a contact in the phone book.
#     """
#     temp = linked_list.head
#     input_name = str(input("Please enter the registered name whose information you want to update: "))
#     check = False
#     while temp:
#         if temp.data.name == input_name:
#             check = True
#             break
#         temp = temp.next
#
#     if check is not True:
#         print(f"{input_name} name not found in phone book")
#         return
#
#     input_new_name = str(input(f"Enter the new name of {input_name} you want to update: (Press enter for no change)"))
#
#     input_new_number = str(
#         input(f"Enter the new number of {input_name} you want to update: (Press enter for no change)"))
#
#     temp.data.name = input_new_name or temp.data.name
#     temp.data.number = input_new_number or temp.data.number
#     print(f"{temp.data.name}: {temp.data.number}")
#
#


# def reset(linked_list: DoublyLinkedList):
#     """
#     It deletes all data and creates a new phone book.
#     """
#     variable = input("This operation will delete all record information in the phone book. Press \"1\" to perform the "
#                      "reset.\nPress any key to cancel")
#     if variable == 1:
#         linked_list.head = None
#
#
# def load_records(linked_list: DoublyLinkedList):
#     global delimiter_line
#     global delimiter_word
#     global txt_name
#     txt_name = "phonebook.txt"
#     delimiter_line = "\n"
#     delimiter_word = ","
#
#     if os.path.isfile(txt_name):
#         txt_name = txt_name
#         with open(file=txt_name, mode="r") as file:
#             records = file.read()
#             records = records.split(delimiter_line)
#             for r in records[:-1]:
#                 name, number = r.split(delimiter_word)
#                 new_record = Record(name=name, number=number)
#                 new_node = Node(data=new_record)
#                 linked_list.add(new_node)
#
#
# def save(linked_list: DoublyLinkedList):
#     temp = linked_list.head
#     with open(file=txt_name, mode="w") as file:
#         while temp:
#             file.write(f"{temp.data.name}{delimiter_word}{temp.data.number}{delimiter_line}")
#             temp = temp.next
#
#
# def menu():
#     print(colored("↓ Select the Action you want to use ↓", "green", attrs=['bold']))
#     print(colored("1- View contacts in the phone book.\n"
#                   "2- Add a new contact to the phone book.\n"
#                   "3- Delete a contact in the phone book.\n"
#                   "4- Update the information of a contact in the phone book.\n"
#                   "5- Searching the phone book by name.\n"
#                   "6- Reset phone book.\n"
#                   "7- Exit", attrs=['bold']))
#
#
# def help_me():
#     print("Please press 1,2,3,4,5 or 6 according to the operation you want to do.")
#     time.sleep(2)
#     input("Press any key to continue")
#
#
# def interface(linked_list: DoublyLinkedList):
#     print(colored(">>>>>>>>Welcome to Phone Book<<<<<<<<", "yellow", attrs=['bold']))
#
#     load_records(linked_list)
#     action = 0
#     while action != "7":
#
#         menu()
#         action = str(input())
#
#         if action == "1":
#             linked_list.show()
#             input("Press any key to continue")
#
#         elif action == "2":
#             add_record(linked_list)
#             input("Press any key to continue")
#
#         elif action == "3":
#             remove_record(linked_list)
#             input("Press any key to continue")
#
#         elif action == "4":
#             update(linked_list)
#             input("Press any key to continue")
#
#         elif action == "5":
#             search_prefix(linked_list)
#             input("Press any key to continue")
#
#         elif action == "6":
#             reset(linked_list)
#
#         elif action == "7":
#             save(linked_list)
#
#         else:
#             help_me()

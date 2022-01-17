from linked_list import LinkedList, Node
from record import Record
from phone_book_operations import add_record, remove_record, update, search_prefix
from termcolor import colored

if __name__ == '__main__':
    r1 = Record(name="Selman", number="541")
    r2 = Record(name="Mustafa", number="542")
    r1_node = Node(data=r1)
    r2_node = Node(data=r2)
    phone_book = LinkedList()
    phone_book.head = r1_node
    r1_node.next = r2_node

    print(colored(">>>>>>>>Welcome to Phone Book<<<<<<<<", "yellow", attrs=['bold']))
    while True:
        print(colored("↓ Select the Action you want to use ↓", "green", attrs=['bold']))
        print(colored("1- View contacts in the phone book.\n2- Add a new contact to the phone book."
                      "\n3- Delete a contact in the phone book.\n4- Update the information of a contact in the phone "
                      "book. "
                      "\n5- Searching the phone book by name.\n6- Exit", attrs=['bold']))

        action = str(input())

        if action == "1":
            phone_book.show()
            print(colored("\n1- Take another action.\n2- Exit.", "red", attrs=['bold']))
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break

        if action == "2":
            add_record(phone_book)
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break

        if action == "3":
            remove_record(phone_book)
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break

        if action == "4":
            update(phone_book)
            print("\n1- Take another action.\n2- Exit.")
            check = str(input())
            if check == "1":
                continue
            if check == "2":
                break

        if action == "5":
            search_prefix(phone_book)
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

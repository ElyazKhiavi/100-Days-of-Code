# Project 1: Personal Phonebook


phone_book = {}


def add_contact():
    while True:
        name = input("Enter name: ")
        number = input("Enter number: ")
        if name in phone_book:
            overwrite = input(
                f"Do you want to overwrite the{name}'s number? y/n: "
            ).lower()
            if overwrite == "y":
                phone_book[name] = number
                break
            else:
                print("Okay fill in the information again.")
                continue
        else:
            phone_book[name] = number  # new contact, add directly
        break
    print("Contact added successfully!")



def lookup():
    name = input("Enter name: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name: ")
    if name in phone_book:
        phone_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def list_all():
    if phone_book:
        print(" --- Phonebook Contacts ---")
        num = 0
        for people, number in phone_book.items():
            num += 1
            print(f" - {num} - {people}: {number}")
    else:
        print("Phonebook is empty!")


while True:
    while True:
        answer = input("""
Phonebook ☎️
- 1. Add contact
- 2. Look up
- 3. List all
- 4. Delete
- 5. Quit
==> Choose: """)
        if answer.isdigit():
            answer = int(answer)
            break
        else:
            print("Enter in a digit.")
    if answer == 1:
        add_contact()
    elif answer == 2:
        lookup()
    elif answer == 3:
        list_all()
    elif answer == 4:
        delete_contact()
    elif answer == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

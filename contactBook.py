# Contact Book - Python Mini Project

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        self.contacts[name] = phone
        print("Contact added")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found")
        else:
            print("\nContact List:")
            for name, phone in self.contacts.items():
                print(name, "-", phone)

    def search_contact(self):
        name = input("Enter name to search: ")
        if name in self.contacts:
            print("Phone Number:", self.contacts[name])
        else:
            print("Contact not found")

    def delete_contact(self):
        name = input("Enter name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")


# Main Program
book = ContactBook()

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book.add_contact()
    elif choice == "2":
        book.view_contacts()
    elif choice == "3":
        book.search_contact()
    elif choice == "4":
        book.delete_contact()
    elif choice == "5":
        print("Program Ended")
        break
    else:
        print("Invalid choice")

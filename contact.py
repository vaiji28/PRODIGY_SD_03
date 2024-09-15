import json
import os

# File where contacts will be stored
CONTACTS_FILE = "contacts.json"


# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}


# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully.")
    save_contacts(contacts)


# View all contacts
def view_contacts(contacts):
    if contacts:
        print("\nContacts List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")
    

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the contact name to edit: ")
    if name in contacts:
        print(f"Current Info - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        
        print(f"Contact '{name}' updated successfully.")
        save_contacts(contacts)
    else:
        print("Contact not found.")


# Delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
        save_contacts(contacts)
    else:
        print("Contact not found.")


# Main menu for contact manager
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit a Contact")
        print("4. Delete a Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()

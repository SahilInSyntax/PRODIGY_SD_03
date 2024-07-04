import json

class ContactManagementSystem:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def edit_contact(self, index, name=None, phone=None, email=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index]['name'] = name
            if phone:
                self.contacts[index]['phone'] = phone
            if email:
                self.contacts[index]['email'] = email
            self.save_contacts()
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            self.save_contacts()
        else:
            print("Invalid contact index.")

def main():
    cms = ContactManagementSystem()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            cms.add_contact(name, phone, email)
        elif choice == '2':
            cms.view_contacts()
        elif choice == '3':
            cms.view_contacts()
            index = int(input("Enter the contact index to edit: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            cms.edit_contact(index, name if name else None, phone if phone else None, email if email else None)
        elif choice == '4':
            cms.view_contacts()
            index = int(input("Enter the contact index to delete: ")) - 1
            cms.delete_contact(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

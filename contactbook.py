import pickle

def print_contacts(contact_book):
    for key, value in contact_book.items():
        print(f"{key}: {value}")

def main():
    contact_book = {}

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Save and Exit")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            name = input("Enter the contact name: ")
            phone = input("Enter the contact phone number: ")
            contact_book[name] = phone
            print("Contact added!")

        elif choice == '2':
            print("\nContacts:")
            print_contacts(contact_book)

        elif choice == '3':
            with open("contact_book.pickle", "wb") as f:
                pickle.dump(contact_book, f)
            print("Contact book saved!")
            break

        elif choice == '4':
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
def view_contacts(file_name):
    contacts = open(file_name,'r')
    print(contacts)
    
#def add_contact():

#def update_contact():

#def delete_contact():

#def search_contact():

def main():
    file_name = 'contacts.txt'
    while True:
        print("\nContact Management System")
        print("1. View all contacts")
        print("2. Add a new contact")
        print("3. Search for a contact ")
        print("4. Update an existing contact ")
        print("5. Delete a contact ")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_contacts(file_name)
        elif choice == '2':
            add_contact(file_name)
        elif choice == '3':
            update_contact(file_name)
        elif choice == '4':
            delete_contact(file_name)
        elif choice == '5':
            search_contact(file_name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


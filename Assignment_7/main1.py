def view_contacts(file_name):
    contacts = open(file_name,'r')
    lines = contacts.readlines()
    for line in lines:
        print(line)
    
def add_contact(file_name, lines):
    contacts = open(file_name,'a')
    name = input("What is the name of your contact? \n")
    while True:
        phone_number = input("What is the phone number of your contact? \n")
        try:
            int_phone_number = int(phone_number)
            if len(phone_number) == 10:
                break
            else:
                print("Please input phone number of 10 digits.")
        except ValueError:
            print("Invalid input. Please enter numbers not letters.")   
            
    if '-' not in phone_number:
        phone_number = f"{phone_number[0:3]}-{phone_number[3:6]}-{phone_number[6:]}"
    contacts.write(f"{lines + 1}, {name}, {phone_number}\n")
    
def update_contact(file_name):
    contacts = open(file_name,'r')
    while True:
        full_name = input("Please enter full name\n")
        if " " in full_name:
            break
        else:
            print("Please enter first and last name.")
    while True:
        new_number = input("What is the new phone number of your contact? \n")
        try:
            int_phone_number = int(new_number)
            if len(new_number) == 10:
                break
            else:
                print("Please input phone number of 10 digits.")
        except ValueError:
            print("Invalid input. Please enter numbers not letters.")
    lines = contacts.readlines()
    new_contact = open(file_name, 'w')
    newLines = ''
    flag = False
    for line in lines:
        if full_name in line and flag == False:
            flag = True
            for word in line:
                if '-' in word:
                    old_number = word
                    if '-' not in new_number:
                        line = line.replace(old_number, f"{new_number[0:3]}-{new_number[3:6]}-{new_number[6:]}")
                    else:
                        line = line.replace(old_number, new_number)
        newLines += line  
    if flag == False:
        lines = len(contacts.readlines())
        newLines += f'{lines + 1}, {full_name}, {new_number}\n'
    new_contact.write(newLines)
    
        
    
        
#def delete_contact():

#def search_contact():

def main():
    file_name = 'Assignment_7/contacts.txt'
    while True:
        print("\nContact Management System")
        print("1. View all contacts")
        print("2. Add a new contact")
        print("3. Search for a contact ")
        print("4. Update an existing contact ")
        print("5. Delete a contact ")
        print("6. Exit")
        choice = input("Enter your choice: ")
        #some of the choices did not correctly corespond to the number choice, so I edited it
        if choice == '1':
            view_contacts(file_name)
        elif choice == '2':
            contacts = open(file_name,'r')
            lines = len(contacts.readlines())
            add_contact(file_name, lines)
        elif choice == '3':
            search_contact(file_name)
        elif choice == '4':
            update_contact(file_name)
        elif choice == '5':
            delete_contact(file_name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


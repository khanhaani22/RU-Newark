def view_contacts(file_name):
    contacts = open(file_name,'r')
    lines = contacts.readlines()
    for line in lines:
        print(line)
    contacts.close()

def add_contact(file_name):
    contacts = open(file_name, 'r')
    num_lines = 0
    lines = contacts.readlines()
    for line in lines:
        num_lines += 1
    new_contacts = open(file_name, 'a')
    while True:
        full_name = input("Please enter full name of person to add to contacts.")
        if " " not in full_name:
            print("Please try again, and enter first name and last name.")
        else:
            while True:
                number = input("Please enter the phone number")
                if '-' in number: 
                    number = number.replace('-', '')
                if len(number) != 10:
                    print("Phone number is greater than 10 digits. Please try again.")
                try:
                    int_number = int(number)
                except ValueError:
                    print("Please input number with only digits.")
                if len(number) == 10: 
                    break
            break
    new_contacts.write(f'{num_lines + 1}, {full_name}, {number[0:3]}-{number[3:6]}-{number[6:]}\n')
    new_contacts.close()
            
def update_contact(file_name):
    while True:
        full_name = input("Please enter full name of person to update.")
        if " " not in full_name:
                print("Please try again, and enter first name and last name.")
        else:
            while True:
                number = input("Please enter the new phone number")
                if '-' in number: 
                    number = number.replace('-', '')
                if len(number) != 10:
                    print("New phone number is greater than 10 digits. Please try again.")
                try:
                    int_number = int(number)
                except ValueError:
                    print("Please input number with only digits.")
                if len(number) == 10: 
                    break
            break
    with open(file_name, 'r') as contacts:
        lines = contacts.readlines()
    
    with open(file_name, 'w') as new_contacts:
        num_lines = 0
        flag = False
        for line in lines:
            num_lines += 1
            if full_name in line and not flag:
                flag = True
                updated_line = f"{num_lines}, {full_name}, {number[:3]}-{number[3:6]}-{number[6:]}\n"
                new_contacts.write(updated_line)
            else:
                new_contacts.write(line)
        
        if not flag:
            print(f"Contact with name {full_name} not found. We will add this new number at the end of file.")
            new_contacts.write(f'{num_lines + 1}, {full_name}, {number[:3]}-{number[3:6]}-{number[6:]}\n')

def search_contact(file_name):
    while True:
        full_name = input("Please enter full name of person to search for.")
        if " " not in full_name:
                print("Please try again, and enter first name and last name.")
        else:
            break
    contacts = open(file_name, 'r')
    lines = contacts.readlines()
    flag = False
    for line in lines:
        if full_name in line:
            flag = True
            print("We have found person in contact list")
            break
    if flag == False:
        print("We did not find person in contacts.")

def delete_contact(file_name):
    while True:
        full_name = input("Please enter full name of person to delete fron contacts.")
        if " " not in full_name:
                print("Please try again, and enter first name and last name.")
        else:
            break
    contacts = open(file_name, 'r')
    lines = contacts.readlines()
    with open(file_name, 'w') as new_contacts:
        num_lines = 0
        for line in lines:
            num_lines += 1
            if full_name in line:
                line = ''
                num_lines = num_lines - 1
            else:
                if str(num_lines) in line[0:1]:
                    updated_line = line
                    new_contacts.write(updated_line)
                else:
                    updated_line = f'{num_lines} {line[1:]}'
                    new_contacts.write(updated_line)
    contacts.close()

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

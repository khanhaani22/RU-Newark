def main():
    acc_num = input("Account number of account you would like to access: ")
    with open('Assignment 8/charge_accounts.txt','r') as file:
        contents = file.read()
        list = contents.split()
        if acc_num in list:
            print("Account ID found.")
        else:
            print("Account ID not found.")

if __name__ == "__main__":
    main()
    
# OUTPUT
"""
Account number of account you would like to access: 123456
Account ID not found.

Account number of account you would like to access: 7895122
Account ID found.
"""
#
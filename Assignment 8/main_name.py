def main():
    name = input("What name would you like to check for? \n")
    with open('Assignment 8/popular_names.txt','r') as file:
        contents = file.read()
        list = contents.split()
    if name in list:
        print("Name was found!")
    else:
        print("Name not found.")

if __name__ == "__main__":
    main()
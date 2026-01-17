# Initialize an empty dictionary to store phone numbers
phonebook = {}

# Function to initialize or reset the phonebook
def initialize_phonebook():
    global phonebook
    phonebook = {}  # Resets the phonebook to an empty dictionary
    print("Phonebook has been initialized.")

# Function to add a phone number
def add_phone_number(name, phone_number):
    phonebook[name] = phone_number
    print(f"Phone number for {name} added.")

# Function to remove a phone number
def remove_phone_number(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Phone number for {name} removed.")
    else:
        print(f"{name} not found in the phonebook.")

# Function to display the current phonebook
def display_phonebook():
    if phonebook:
        print("\nCurrent Phonebook:")
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")
    else:
        print("Phonebook is empty.")

# Main program loop
while True:
    print("\nPhonebook Menu:")
    print("1. Initialize phonebook")
    print("2. Add phone number")
    print("3. Remove phone number")
    print("4. Display phonebook")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        initialize_phonebook()
    elif choice == '2':
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        add_phone_number(name, phone_number)
    elif choice == '3':
        name = input("Enter the name to remove: ")
        remove_phone_number(name)
    elif choice == '4':
        display_phonebook()
    elif choice == '5':
        print("Exiting phonebook database.")
        break
    else:
        print("Invalid choice. Please try again.")


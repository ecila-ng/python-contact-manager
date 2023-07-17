########################################################################
# Tran Nguyen - Question 2 Lab 2
#
# This program allows you to store the contact list in a file named
# contact.txt
########################################################################

import os

# Constants for the menu choices
ADD_CHOICE = 1
SHOW_CHOICE = 2
SEARCH_CHOICE = 3
MODIFY_CHOICE = 4
DELETE_CHOICE = 5
QUIT_CHOICE = 6


# The main function.
def main():
    choice = 0

    while choice != QUIT_CHOICE:
        # Display the menu
        print('  CHOICE MENU  ')
        print('1) Add a contact')
        print('2) Show the list of contacts')
        print('3) Search for a name in the list')
        print('4) Modify a contact')
        print('5) Delete a contact from the list')
        print('6) Quit')

        # Ask for the user's choice
        choice = int(input('Enter your choice: '))

        # Perform the selected choice
        if choice == ADD_CHOICE:
            add()
        elif choice == SHOW_CHOICE:
            show()
        elif choice == SEARCH_CHOICE:
            search()
        elif choice == MODIFY_CHOICE:
            modify()
        elif choice == DELETE_CHOICE:
            delete()
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: Invalid selection.')


def add():
    # Create a variable to control the loop.
    keep_going = 'y'

    # Open the contact.txt file in append mode.
    contact_file = open('contact.txt', 'a')

    # Add records to the file.
    while keep_going == 'y' or keep_going == 'Y':
        print('Enter the following contact info:')
        name = input('Name: ')
        email = input('Email: ')
        phone = input('Phone: ')

        # Append the record to the file.
        contact_file.write(name + '\n')
        contact_file.write(email + '\n')
        contact_file.write(phone + '\n')

        # Ask if the user wants to add another record
        print('Do you want to add another record?')
        keep_going = input('Y = yes, anything else = no: ')

    # Close the file.
    contact_file.close()
    print('Contacts added to contact.txt.')


def show():
    try:
        # Open the contact.txt file in read-only mode
        contact_file = open('contact.txt', 'r')

        # Read the first record's name field.
        name = contact_file.readline()
        print('\nList of contact(s):\n')
        # Read the rest of the file.

        i = 1  # This variable keeps track of the number of records

        while name != '':
            # Read the email and phone field.
            email = contact_file.readline()
            phone = contact_file.readline()

            # Strip the \n from the name, email and phone.
            name = name.rstrip('\n')
            email = email.rstrip('\n')
            phone = phone.rstrip('\n')

            # Display the record.
            print(f'Contact #{i}')
            print('    Name:', name)
            print('    Email:', email)
            print('    Phone:', phone)
            print('------------------------')

            # Read the next name.
            name = contact_file.readline()
            i += 1

        # Close the file.
        contact_file.close()

    except IOError as err:
        print(err)


def search():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    kw = input('Enter a name to search for: ')

    # Open the contact.txt file in read-only mode
    contact_file = open('contact.txt', 'r')

    # Read the first record's name field.
    name = contact_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the email and phone field.
        email = contact_file.readline()
        phone = contact_file.readline()

        # Strip the \n from the name, email and phone.
        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone = phone.rstrip('\n')

        # Determine whether this record matches
        # the search value.
        if name == kw:
            # Display the record.
            print('Name: ', name)
            print('Email: ', email)
            print('Phone: ', phone)
            print()
            # Set the found flag to True.
            found = True

        # Read the next name.
        name = contact_file.readline()

    # Close the file.
    contact_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print('Contact not found.')
        print()


def modify():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    kw = input('Enter a name to search for update: ')
    new_email = input('Enter the new email for update: ')
    new_phone = input('Enter the new phone for update: ')

    # Open the contact.txt file.
    contact_file = open('contact.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's name field.
    name = contact_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the email and phone field.
        email = contact_file.readline()
        phone = contact_file.readline()

        # Strip the \n from the name, email and phone.
        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone = phone.rstrip('\n')

        # If this is the updated one, write updated info to temp file
        # If not, write the original info to temp file
        if name == kw:
            # Write the modified record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(new_email + '\n')
            temp_file.write(new_phone + '\n')

            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')

        # Read the next name.
        name = contact_file.readline()

    # Close the contact file and the temporary file.
    contact_file.close()
    temp_file.close()

    # Delete the original contact.txt file.
    os.remove('contact.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'contact.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
        print()
    else:
        print('Contact not found.')
        print()


def delete():
    # Create a bool variable to use as a flag.
    found = False

    # Get the value to delete.
    kw = input('Which name do you want to delete? ')

    # Open the contact.txt file
    contact_file = open('contact.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's name field.
    name = contact_file.readline()

    # Read the rest of the file.
    while name != '':
        # Read the email and phone field.
        email = contact_file.readline()
        phone = contact_file.readline()

        # Strip the \n from the name, email and phone.
        name = name.rstrip('\n')
        email = email.rstrip('\n')
        phone = phone.rstrip('\n')

        # If this is not the record to delete, then
        # write it to the temporary file.
        if name != kw:
            # Write the record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next name.
        name = contact_file.readline()

    # Close the contact file and the temporary file.
    contact_file.close()
    temp_file.close()

    # Delete the original contact.txt file.
    os.remove('contact.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'contact.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
        print()
    else:
        print('Contact not found.')
        print()


if __name__ == '__main__':
    main()

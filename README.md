# python-contact-manager
📃 An interactive Python program that keeps track of contacts. Prompt user for commands.

Filename: main.py

Completed: 06/25/2023

Platform developed: Windows 11, PyCharm CE 2023

## problem statement: 
The program should essentially prompt the user to enter a command, and process the command as follows:

#### 1 (add):
This option allows the user to add a new contact to the contact list. The user will be prompted to enter the details of the contact, such as the name, phone number, and email address. 
Once entered, the contact will be saved to the 'contact.txt' file.

#### 2 (show):
Choosing this option will display the entire list of contacts stored in the 'contact.txt' file. The program will retrieve the contacts and present them in a formatted manner, showing the name, phone number, and email address for each contact.

#### 3 (search):
This choice enables the user to search for a specific contact by entering the name. The program will search the contact list for any matches and display the details of the matching contacts, including the name, phone number, and email address.

#### 4 (modify):
If the user wants to update the information of a specific contact, they can select this option. The user will be prompted to enter the name of the contact they want to modify. 
Once the contact is found, the program will allow the user to update the contact's details, such as the phone number or email address. The modified contact will be saved back to the 'contact.txt' file.

#### 5 (delete):
This option allows the user to remove a contact from the contact list. The user will be asked to enter the name of the contact they want to delete. 
If the contact exists in the list, it will be deleted from the 'contact.txt' file, effectively removing it from the contact management system.

#### 6 (quit), which should stop the running program.

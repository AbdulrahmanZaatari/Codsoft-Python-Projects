# Simple Calculator 🧮

## Description
This is a basic calculator program written in Python, providing options for addition ➕, subtraction ➖, multiplication ✖️, and division ➗. The program includes error handling for division by zero.

## Functions
- **summ(x, y):**
  Adds two numbers, x and y, and returns the result.
  
- **multiply(x, y):**
  Multiplies two numbers, x and y, and returns the product.
  
- **division(x, y):**
  Divides two numbers, x and y, and returns the result.
  Handles the case where the denominator (y) is zero and provides an error message.
  
- **subtract(x, y):**
  Subtracts the second number, y, from the first number, x, and returns the difference.
  
- **menu():**
  Displays a menu of available operations (addition, subtraction, multiplication, division, exit).
  
- **displayMenu():**
  Greets the user and prompts them to choose an operation.
  Takes user input for the operation and performs the corresponding calculation.
  Continues until the user chooses to exit.

- **main():**
  Invokes the displayMenu() function to start the calculator.

## Usage
1. Run the script.
2. Enter your name when prompted.
3. Choose an operation by entering the corresponding number or symbol.
4. Enter the required numbers for the chosen operation.
5. View the result.

## Note
Make sure to enter valid numeric inputs, and the program will handle the selected operation accordingly. 🚀

---

# Contact List Manager 📇

## Description
This is a simple Contact List Manager implemented in Python using the tkinter library for the graphical user interface. The program allows users to add, view, delete, search, and update contacts. Each contact has an ID, name, phone number, email, and address.

## Classes
- **Contact:**
  Represents a single contact with attributes such as ID, name, phone number, email, and address.
  `__str__` method provides a formatted string representation of the contact.
  
- **Contact_Book:**
  Manages the contact list and GUI interactions.
  Includes methods for adding, viewing, deleting, searching, and updating contacts.
  Utilizes tkinter for the graphical user interface.

## UI Elements
- **Listbox:** Displays the list of contacts.
- **Scrollbar:** Enables scrolling in the listbox.
- **Buttons:**
  - "Add contact": Adds a new contact to the list.
  - "Delete contact": Deletes the selected contact from the list.
  - "View contacts": Displays the list of contacts.
  - "Search Contacts": Searches for contacts based on name or phone number.
  - "Update Contacts": Updates information for a selected contact.

## Usage
1. Run the script.
2. The main window opens with buttons for various operations.
3. Click on the buttons to perform actions like adding, deleting, viewing, searching, or updating contacts.
4. Dialog boxes prompt for input when adding, searching, or updating contacts.

## Note
The program uses tkinter for the GUI, and it's recommended to run it in a local Python environment. 📞✉️

---

# Password Generator 🛡️

## Description
This is a simple password generator script written in Python. It generates strong passwords of a specified length using random characters. The program interacts with the user, allowing them to create multiple passwords and exit the system.

## Functions
- **crp(x):**
  Generates a random password of length x using ASCII characters between 33 and 126.

## Usage
1. Run the script.
2. Enter your name when prompted.
3. The program greets you and prompts you to create a powerful password.
4. Input the desired length for your password.
5. A randomly generated password is displayed.
6. The program asks if you want to create another password.
  - If "Yes," repeat steps 4-5 for a new password.
  - If "No," the last password is displayed, and the system exits.

## Note
The generated passwords include a mix of symbols, numbers, and letters to enhance security. Make sure to store generated passwords securely. 🔐💪

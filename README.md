#  Guest List Manager

A simple command-line Python application to manage a guest list for an event. It allows users to add, view, delete, update, sort, and search guests interactively.

---

##  Features

-  Add a new guest  
-  View all guests  
-  Delete guest by name or position  
-  Search for a guest  
-  Update a guest’s name  
-  Total number of guests  
-  Sort guests alphabetically  
-  Quit the application

---

##  Getting Started

###  Requirements

- Python 3.x

###  How to Run

```bash
python guest_list_manager.py
```
###  Demo
```bash
Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 1  

Enter the Guest Name: venky
venky has been inserted successfully

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 1

Enter the Guest Name: anu
anu has been inserted successfully

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 1

Enter the Guest Name: ravi
ravi has been inserted successfully

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 2

-------------------------------
Guest List is as follows: 
1.venky
2.anu
3.ravi
-------------------------------

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 4

Guest List sorted in Alphabetical Order
-------------------------------
Guest List is as follows: 
1.anu
2.ravi
3.venky
-------------------------------

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 5

Enter the Guest Name to Search: ramu
Sorry! ramu is not part of the Guest List
Do you want to add this as a Guest? [yes / no] : no
Ok, your choice !

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 3

Do you want to delete based on 
a. Value
b.Position
Your Choice [a/b]: a
Enter the Guest Name to be removed: venky
venky has been successfully removed

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 6

1.anu
2.ravi
Enter the index value you want to update: 1
Enter the Updated Name: anuradha
Data updated Successfully

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 2

-------------------------------
Guest List is as follows: 
1.anuradha
2.ravi
-------------------------------

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 7

Total Number of Guests coming to the Party = 2

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 5

Enter the Guest Name to Search: bujji
Sorry! bujji is not part of the Guest List
Do you want to add this as a Guest? [yes / no] : yes
bujji has been inserted successfully

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 7

Total Number of Guests coming to the Party = 3

Welcome to the Guest List Manager App
1. Add a New Guest
2. View the Guest List
3. Delete a Guest
4. Guest List in Alphabetical order
5. Search for a Guest
6. Update the Guest Name
7. Total Number of Guest coming
8. Quit
Enter your choice [1 to 8]: 8
Thank you for using our Application
```
##  Code Overview

- **Data Storage**: Python list `guest_list[]`
- **Menu Interface**: Infinite `while` loop
- **Functions Used**: `append()`, `remove()`, `pop()`, `sort()`, `len()`
- **User Input**: Supports name and position-based actions

---

##  Future Enhancements

- Save guest list to a file (CSV or JSON)
- Load guest list from a saved file
- GUI version using Tkinter or PyQt
- Email guests (via SMTP integration)

# Empty List
guest_list = []

# Menu Options
while True:
    print("Welcome to the Guest List Manager App")
    print("1. Add a New Guest")
    print("2. View the Guest List")
    print("3. Delete a Guest")
    print("4. Guest List in Alphabetical order")
    print("5. Search for a Guest")
    print("6. Update the Guest Name")
    print("7. Total Number of Guest coming")
    print("8. Quit")

    # User Choosing the option of their choice
    opt = int(input("Enter your choice [1 to 8]: "))

    # INSERTION
    if opt == 1:
        print()
        # Reading the Guest Name from the User
        name = input("Enter the Guest Name: ")
        # append() Function to insert the data (insertion)
        guest_list.append(name)
        # After insertion - printing a success message
        print(F"{name} has been inserted successfully")
        print()
       
    # VIEWING / DISPLAY
    elif opt == 2:
        # Traversal - displayiny the content of the list
        print()
        # If the List is Empty - this code will get executed
        if len(guest_list) == 0:
            print("There are no Guests coming to the Party")
        # If the List contains value - this code will get executed
        else:
            print("-------------------------------")
            print("Guest List is as follows: ")
            for i,v in enumerate(guest_list):
                print(F"{i+1}.{guest_list[i]}")
            print("-------------------------------")
        print()
   
    # DELETION
    elif opt == 3:
        print()
        s = input("Do you want to delete based on \na. Value\nb.Position\nYour Choice [a/b]: ").lower()
       
        match s:
            case 'a':
                # value based deletion
                name = input("Enter the Guest Name to be removed: ")
                # Checking whether the name is present in the List
                if name in guest_list:
                    guest_list.remove(name)
                    print(F"{name} has been successfully removed")
                    print()
                else:
                    print(F"{name} is not present in the Guest List")
                    print()

            case 'b':
                # index based deletion
                x = int(input("Enter the Position Number to delete: "))
                # Checking if the given position number is valid
                if x <= len(guest_list):
                    x=x-1
                    name = guest_list.pop(x)
                    print(F"{name} has been deleted successfully")
                    print()
                else:
                    print("Invalid Position Entered. Pls view the data and enter a number correctly")
                    print()

            case _: print("Invalid Option")
               
    # SORTING
    elif opt == 4:
        print()
        # alphabetical sorting - ascending order
        alpha = sorted(guest_list)
        print("Guest List sorted in Alphabetical Order")
        print("-------------------------------")
        print("Guest List is as follows: ")
        for i,v in enumerate(alpha):
            print(F"{i+1}.{alpha[i]}")
        print("-------------------------------")
        print()
   
    # SEARCHING
    elif opt == 5:
        print()
        name = input("Enter the Guest Name to Search: ")
        if name in guest_list:
            print(F"{name} is a Guest at the Event")
            print()
        else:
            print(F"Sorry! {name} is not part of the Guest List")
            ans = input("Do you want to add this as a Guest? [yes / no] : ").lower()
            if ans == 'yes':
                guest_list.append(name)
                print(F"{name} has been inserted successfully")
                print()
            else:
                print("Ok, your choice !")
                print()
   
    # UPDATION
    elif opt == 6:
        print()
        for i,v in enumerate(guest_list):
            print(F"{i+1}.{guest_list[i]}")
        x = int(input("Enter the index value you want to update: "))
        if x <= len(guest_list):
            x = x - 1
            name = input("Enter the Updated Name: ")
            guest_list[x] = name
            print("Data updated Successfully")
            print()
        else:
            print("Invalid index given")
            print()
   
    # TOTAL GUESTS
    elif opt == 7:
        print()
        n = len(guest_list)
        # Checking if the Guest List is Empty or not
        if n == 0:
            print(F"There are no Guest names in the List")
            print()
        else:
            print(F"Total Number of Guests coming to the Party = {n}")
            print()
   
    # QUIT
    elif opt == 8:
        print("Thank you for using our Application")
        break
   
    else:
        print("Invalid input. Try again")
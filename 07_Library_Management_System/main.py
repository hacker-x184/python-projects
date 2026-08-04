from Book import *
from choice import *
from members import *
print("Welcome to our library😁!")
in_library = int(input("Your Want to use the library fuctions   :-\n1. -  Yes\n2. -  No :---"))
if in_library==1:
    in_library = True
else:
    in_library=False
    print("Thanks for Visting Our System 😊")
try:
    while in_library:
        user_choice = int(input("1 -   Add Book\n2 -   Remove Book\n3 -   Borrow Book\n4 -   Return Book\n5 -   Search Book\n6 -   Display Books\n7 -   Add Members\n8  -  Exit\nEnter Your Choices here:-"))
        if user_choice == 1:
            choice_1()
        elif user_choice == 2:
            choice_2()
        elif user_choice == 3:
            choice_3()
        elif user_choice == 4:
            choice_4()
        elif user_choice == 5:
            choice_5()
        elif user_choice == 6:
            choice_6()
        elif user_choice == 7:
            choice_7()
        elif user_choice == 8:
            in_library=False
            print("Thnx for Coming 🫡")
        else:
            print("User Selected the invalid operation:-)\nNow exit the library")
            in_library=False
except Exception:
    print("")
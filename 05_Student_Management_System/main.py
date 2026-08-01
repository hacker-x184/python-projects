def add_st(dict,name,marks):
    dict[name]=marks    
    print(f"Adding the Student {name} are Susseceful")
def update_mark(dict,name,mark):
    if name in dict:
        dict[name] = mark
        print(f"Marks update succesfuly")
def del_student(dict,name):
    dict.pop(name)
    print(f"Removing the Student Sussesful")
def search_student(dict,name):
    for i in dict:
        if name==i:
            print(f"Here is the name of the student :-{name}:{dict[i]}")
def display_all(dict):
    for name,marks in dict.items():
        print(f"{name}:{dict[name]}")
def avg(dict):
    total = 0
    for i in dict:
        total = total + dict[i]
    print(f"Average marks of the Students{total/len(dict)}")
student_dict = {
"Luffy":20,
"Zoro":70,
"Sanji":99,
"Naruto":45
}
more = True
while more:
    user_choice=int(input("===== Student Management System =====\n1. Add Student\n2. Update Marks\n3. Delete Student\n4. Search Student\n5. Display All Students\n6. Average Marks\n7. Exit\nEnter Choice:-"))
    if user_choice == 1:
        name = input("Enter name here :-")
        mark = int(input("Enter marks here :-"))
        add_st(student_dict,name,mark)
    elif user_choice == 2:
        name = input("Enter name of student ther  marks you want to change :-")
        mark = int(input("Enter marks that you want to update here :-"))    
        update_mark(student_dict,name,mark)
    elif user_choice == 3:
        name = input("Enter name here that you want to delete :-")
        del_student(student_dict,name)
    elif user_choice == 4:
        name = input("Enter name here that you want to Search :-")
        search_student(student_dict,name)
    elif user_choice == 5:
        display_all(student_dict)
    elif user_choice == 6:
        avg(student_dict)
    else :
        more = False

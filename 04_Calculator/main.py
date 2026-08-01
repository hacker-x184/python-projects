def add (a,b):
    b = a+b
    return b
def sub (a,b,c=1):
    if c == 2:
        b= b-a
    else:
        b = a-b
    return b
def multi (a,b):
    b = a*b
    return b
def div (a,b,c=1):
    try:
        if c==2:
            b = b/a
        else:    
            b=a/b
        return b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        
user_selection = input("(+)   -   Addition\n(-)   -   Subtraction\n(*)   -   Multiplication\n(/)   -   Division\nSelect One of the operations:-")
num_1 = int(input("Enter Number 1 Here:-"))
num_2 = int(input("Enter Number 2 Here:-"))
c = 1
b = 0
while True:
    try:
        if user_selection in ["+", "-", "*", "/"]:
            if user_selection=="+":
                b = add(num_1,num_2)
                print(b)
            elif user_selection == "-":
                b = sub(num_1,num_2,c)
                print(b)
            elif user_selection == "*":
                b = multi(num_1,num_2)
                print(b)
            elif user_selection == "/":
                b = div(num_1,num_2,c)
                print(b)
            num_2 = b
        else:
            break
        user_selection = input("(+)   -   Addition\n(-)   -   Subtraction\n(*)   -   Multiplication\n(/)   -   Division\nSelect One of the operations:-")
        num_1 = int(input("Enter Number 1 Here:-"))
        c = 2
    except Exception:
        print("User Selected a wrong Operation")
        break
print(f"Your Final b is = {b}")
import random

print("Welcome to our Rock, Paper, Scissors game :-)")

match = int(input("Enter number of matches you want to play: "))

score = 0
i = 0

while i < match:

    user = input("\nType 'r' for Rock, 'p' for Paper, 's' for Scissors: ")

    if user == 'r':
        user = "Rock"
    elif user == 'p':
        user = "Paper"
    elif user == 's':
        user = "Scissors"
    else:
        print("Invalid choice")
        continue

    com = random.randint(1,3)

    if com == 1:
        com = "Rock"
    elif com == 2:
        com = "Paper"
    else:
        com = "Scissors"

    print("Computer chose:", com)

    if user == com:
        print("It's a tie!")

    elif (user == "Rock" and com == "Scissors") or \
         (user == "Paper" and com == "Rock") or \
         (user == "Scissors" and com == "Paper"):
        print("You win!")
        score += 1

    else:
        print("Computer wins!")

    i += 1

print("\nYour total score:", score)
print("Thanks for playing! :-) ")
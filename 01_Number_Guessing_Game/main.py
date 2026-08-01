import random
print("Welcome to our gusseing game :-)")
print("your got the three chances for gussing the number that the range did you give us ")
chances = 5
num=int(input("enter the maximum value of your gussing number :---"))
score = 0
if (num<=0):
    print("Next time choose the number graeter than zero")
else:
    com = random.randint(0,num)
    while (0,chances+1):
        num=int(input("Now try to gusse the number :-)"))
        if (num == com):
            print("That's great you are Right ")
            score +=1
            break
        else:
            print("You are Wrong")
            print("Hope your win next time")
            chances -=1
print("Your Total scroe is ",score,"Thnx for playing ")
print("Hope you like it!  :-)")
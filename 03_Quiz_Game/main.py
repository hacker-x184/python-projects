import random
print("Welcome to Our Quiz game! ")
playing = input("Do you want to play? ")
score = 0
if (playing == "no"):
    playing = False
    print("Thnx for coming... :)")
else:
    playing = True
    print("Okay! let's Playy:)")
    while playing:
        val = random.randint(1,20)
        if (val == 1):
            answer = input("What does CPU stand for? ")
            if answer.strip().lower() == "central processing unit":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True 
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
        elif(val == 2):
            answer = input("What does RAM stand for? ")
            if answer.strip().lower() == "random access memory":
                print("Correct")
                score+=1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 3):
            answer = input("What does GPU stand for? ")
            if answer.strip().lower() == "graphics processing unit":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 4):
            answer = input("What does ROM stand for? ")
            if answer.strip().lower() == "read only memory":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 5):
            answer = input("What does HTML stand for? ")
            if answer.strip().lower() == "hypertext markup language":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 6):
            answer = input("What does CSS stand for? ")
            if answer.strip().lower() == "cascading style sheets":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 7):
            answer = input("What does HTTP stand for? ")
            if answer.strip().lower() == "hypertext transfer protocol":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 8):
            answer = input("What does HTTPS stand for? ")
            if answer.strip().lower() == "hypertext transfer protocol secure":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 9):
            answer = input("What does URL stand for? ")
            if answer.strip().lower() == "uniform resource locator":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 10):
            answer = input("What does IP stand for? ")
            if answer.strip().lower() == "internet protocol":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 11):
            answer = input("What does USB stand for? ")
            if answer.strip().lower() == "universal serial bus":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 12):
            answer = input("What does LAN stand for? ")
            if answer.strip().lower() == "local area network":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 13):
            answer = input("What does WAN stand for? ")
            if answer.strip().lower() == "wide area network":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 14):
            answer = input("What does AI stand for? ")
            if answer.strip().lower() == "artificial intelligence":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 15):
            answer = input("What does ML stand for? ")
            if answer.strip().lower() == "machine learning":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 16):
            answer = input("What does API stand for? ")
            if answer.strip().lower() == "application programming interface":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 17):
            answer = input("What does OS stand for? ")
            if answer.strip().lower() == "operating system":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 18):
            answer = input("What does DBMS stand for? ")
            if answer.strip().lower() == "database management system":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 19):
            answer = input("What does IDE stand for? ")
            if answer.strip().lower() == "integrated development environment":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 20):
            answer = input("What does DNS stand for? ")
            if answer.strip().lower() == "domain name system":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 21):
            answer = input("What does SQL stand for? ")
            if answer.strip().lower() == "structured query language":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 22):
            answer = input("What does GUI stand for? ")
            if answer.strip().lower() == "graphical user interface":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 23):
            answer = input("What does CLI stand for? ")
            if answer.strip().lower() == "command line interface":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 24):
            answer = input("What does JSON stand for? ")
            if answer.strip().lower() == "javascript object notation":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 25):
            answer = input("What does XML stand for? ")
            if answer.strip().lower() == "extensible markup language":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 26):
            answer = input("What does CDN stand for? ")
            if answer.strip().lower() == "content delivery network":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 27):
            answer = input("What does SSH stand for? ")
            if answer.strip().lower() == "secure shell":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 28):
            answer = input("What does FTP stand for? ")
            if answer.strip().lower() == "file transfer protocol":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 29):
            answer = input("What does TCP stand for? ")
            if answer.strip().lower() == "transmission control protocol":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True

        elif (val == 30):
            answer = input("What does UDP stand for? ")
            if answer.strip().lower() == "user datagram protocol":
                print("Correct")
                score += 1
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
            else:
                print("Incorrect answer")
                playing = input("Do you want to play? ")
                if (playing == "no"):
                    playing = False
                    break
                    print("Thnx for coming... :)")
                else:
                    playing = True
print("Your Final Secore is ",score,"Thnx for playing")
print("Hope you like it!  :-)")
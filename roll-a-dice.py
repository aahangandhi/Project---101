import random
response = "y"
while(response == "y"):
    option = input("Press Y to Roll the dice and press N to exit: ")
    response = option.lower()
    if(response == "y"):
        number = random.randint(1, 6)
        if(number == 1):
            print("|---------|")
            print("|         |")
            print("|    1    |")
            print("|         |")
            print("|---------|")
        if(number == 2):
            print("|---------|")
            print("|         |")
            print("| 2     2 |")
            print("|         |")
            print("|---------|")
        if(number == 3):
            print("|---------|")
            print("| 3       |")
            print("|    3    |")
            print("|       3 |")
            print("|---------|")
        if(number == 4):
            print("|---------|")
            print("| 4     4 |")
            print("|         |")
            print("| 4     4 |")
            print("|---------|")
        if(number == 5):
            print("|---------|")
            print("| 5     5 |")
            print("|    5    |")
            print("| 5     5 |")
            print("|---------|")
        if(number == 6):
            print("|---------|")
            print("| 6     6 |")
            print("| 6     6 |")
            print("| 6     6 |")
            print("|---------|")                
    else:
        print("Have a nice day!!! :D")
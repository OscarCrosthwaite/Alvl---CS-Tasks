import random
computerActions = ["r", "p", "s"]
playerAction = input("please choose r, p or s")
computerAction = computerActions.random.choice()
if playerAction == "p":
    if computerAction == "p":
        print("Draw!")
    elif computerAction == "r":
        print("Player win!")
    elif computerAction == "s":
        print("Computer win!")
    else:
        print("error")
elif playerAction == "r":
    if computerAction == "p":
        print("Computer win!")
    elif computerAction == "r":
        print("Draw!")
    elif computerAction == "s":
        print("Player win!")
    else:
        print("error")
elif playerAction == "s":
    if computerAction == "p":
        print("Player win!")
    elif computerAction == "r":
        print("Computer win!")
    elif computerAction == "s":
        print("Draw!")
    else:
        print("error")

    
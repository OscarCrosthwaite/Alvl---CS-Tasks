#plays rock, paper, scissors between player-chosen action and random computer action
import random
computerActions = ["r", "p", "s"]
#creates list for computer containing rock, paper and scissors
playerAction = input("Please choose r, p or s: ")
#finds player action
computerAction = random.choice(computerActions)
#randomly chooses computer action
print(f"computer picked {computerAction}")
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
#compares player action with computer action and decides outcome. 
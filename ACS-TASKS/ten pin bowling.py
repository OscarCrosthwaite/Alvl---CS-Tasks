bowlingPoints = 0
rounds = 1
bowlingPins = 0


def pinCount():
    bowlingPins = int(input("How many bowling pins did you knock down?: "))
def nonStrikeScore():
    bowlingPoints = bowlingPoints + bowlingPins
def error():
    print("Error. Try again!")
def roundCount():
    rounds = rounds + 1









while rounds < 11:
    bowlingPins1 = int(input("How many bowling pins did you knock down?: "))
    if bowlingPins1 == 10:
        while True:
            strikeOrSpare1 = input("Was it a strike or a spare?: ")
            if strikeOrSpare1 == "strike":
                bowlingPoints = bowlingPoints + 10
                break
            elif strikeOrSpare1 == "spare":
                bowlingPoints = bowlingPoints + 10
                break
            else:
                error()
                continue
    else:
        bowlingPoints = bowlingPoints + bowlingPins
    roundCount()
    bowlingPins2 = int(input("How many bowling pins did you knock down?: "))
    if bowlingPins2 == 10:
        while True:
            strikeOrSpare2 = input("Was it a strike or a spare")
            if strikeOrSpare2 == "strike" and strikeOrSpare1 == "strike":
                bowlingPoints = bowlingPoints + 20
                break
            elif strikeOrSpare2 == "strike":
                bowlingPoints = bowlingPoints + 10
                break
            elif strikeOrSpare2 == "spare":
                bowlingPoitns = bowlingPoints + 10
                break
            else:
                error()
                continue
    else:
        if bowlingPins1 == 10:
            bowlingPoints = bowlingPoints + bowlingPins2 + 10
        if strikeOrSpare1 == "strike":
            
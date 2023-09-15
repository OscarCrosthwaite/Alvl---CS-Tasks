bowlingPoints = 0
rounds = 1

fact = "false"
strike = "false"
spare = "false"
Pins1 = 0
Pins2 = 0
Pins3 = 0
Pins4 = 0
Pins5 = 0
Pins6 = 0
Pins7 = 0
Pins8 = 0


def factTrue():
    fact = "true"
def error():
    print("Error!")
def roundCount():
    rounds = rounds + 1
def Strike():
    print("Strike!")
    strike = "true"
def Spare():
    print("Spare!")
    spare = "true"
def Double():
    print("Double!")
    strike = "true"
def Turkey():
    print("Turkey!")
    strike = "true"
def FourBagger():
    print("Four-bagger!")
    strike = "true"


while rounds < 11:
    pins1 = int(input("How many bowling pins did you knock down on your first attempt?: "))
    Pins2 = int(input("How many bowling pins did you knock down on your second attempt?: "))
    while fact == "false":
        if Pins1 == 10:
            bowlingPoints = bowlingPoints + 10
            Strike()
            factTrue()
        elif Pins1 == 10 and Pins3 == 10:
            bowlingPoints = bowlingPoints + 20
            Double()
            factTrue()
        elif Pins1 == 10 and Pins3 == 10 and Pins5 == 10:
            Turkey()
            factTrue()
            bowlingPoints = bowlingPoints + 30
        elif Pins1 == 10 and Pins3 == 10 and Pins5 == 10 and Pins7 == 10:
            bowlingPoints = bowlingPoints + 40
            FourBagger()
            factTrue()
        elif Pins1 + Pins2 == 10:
            bowlingPoints = bowlingPoints + 10
            if strike == "true":
                bowlingPoints = bowlingPoints + 10
                strike = "false"
                spare = "false"
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins1
                strike = "false"
                spare = "false"
                factTrue()
        else:
            bowlingPoints = bowlingPoints + Pins1 + Pins2
            if strike == "true":
                bowlingPoints = bowlingPoints + Pins1 + Pins2
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins1
                strike = "false"
                spare = "false"
                factTrue()
            else:
                strike = "false"
                spare = "false"
                factTrue()
    roundCount()
    
    
    pins3 = int(input("How many bowling pins did you knock down on your first attempt?: "))
    Pins4 = int(input("How many bowling pins did you knock down on your second attempt?: "))
    while fact == "false":
        if Pins3 == 10:
            bowlingPoints = bowlingPoints + 10
            Strike()
            factTrue()
        elif Pins3 == 10 and Pins5 == 10:
            bowlingPoints = bowlingPoints + 20
            Double()
            factTrue()
        elif Pins3 == 10 and Pins5 == 10 and Pins7 == 10:
            Turkey()
            factTrue()
            bowlingPoints = bowlingPoints + 30
        elif Pins3 == 10 and Pins5 == 10 and Pins7 == 10 and Pins1 == 10:
            bowlingPoints = bowlingPoints + 40
            FourBagger()
            factTrue()
        elif Pins3 + Pins4 == 10:
            bowlingPoints = bowlingPoints + 10
            if strike == "true":
                bowlingPoints = bowlingPoints + 10
                strike = "false"
                spare = "false"
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins1
                strike = "false"
                spare = "false"
                factTrue()
        else:
            bowlingPoints = bowlingPoints + Pins3 + Pins4
            if strike == "true":
                bowlingPoints = bowlingPoints + Pins3 + Pins4
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins3
                strike = "false"
                spare = "false"
                factTrue()
            else:
                strike = "false"
                spare = "false"
                factTrue()
    roundCount()
    
    
    pins5 = int(input("How many bowling pins did you knock down on your first attempt?: "))
    Pins6 = int(input("How many bowling pins did you knock down on your second attempt?: "))
    while fact == "false":
        if Pins5 == 10:
            bowlingPoints = bowlingPoints + 10
            Strike()
            factTrue()
        elif Pins5 == 10 and Pins7 == 10:
            bowlingPoints = bowlingPoints + 20
            Double()
            factTrue()
        elif Pins5 == 10 and Pins7 == 10 and Pins1 == 10:
            Turkey()
            factTrue()
            bowlingPoints = bowlingPoints + 30
        elif Pins5 == 10 and Pins7 == 10 and Pins1 == 10 and Pins3 == 10:
            bowlingPoints = bowlingPoints + 40
            FourBagger()
            factTrue()
        elif Pins5 + Pins6 == 10:
            bowlingPoints = bowlingPoints + 10
            if strike == "true":
                bowlingPoints = bowlingPoints + 10
                strike = "false"
                spare = "false"
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins5
                strike = "false"
                spare = "false"
                factTrue()
        else:
            bowlingPoints = bowlingPoints + Pins5 + Pins6
            if strike == "true":
                bowlingPoints = bowlingPoints + Pins5 + Pins6
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins5
                strike = "false"
                spare = "false"
                factTrue()
            else:
                strike = "false"
                spare = "false"
                factTrue()
    roundCount()
    
    
    pins7 = int(input("How many bowling pins did you knock down on your first attempt?: "))
    Pins8 = int(input("How many bowling pins did you knock down on your second attempt?: "))
    while fact == "false":
        if Pins7 == 10:
            bowlingPoints = bowlingPoints + 10
            Strike()
            factTrue()
        elif Pins7 == 10 and Pins1 == 10:
            bowlingPoints = bowlingPoints + 20
            Double()
            factTrue()
        elif Pins7 == 10 and Pins1 == 10 and Pins3 == 10:
            Turkey()
            factTrue()
            bowlingPoints = bowlingPoints + 30
        elif Pins7 == 10 and Pins1 == 10 and Pins3 == 10 and Pins5 == 10:
            bowlingPoints = bowlingPoints + 40
            FourBagger()
            factTrue()
        elif Pins7 + Pins8 == 10:
            bowlingPoints = bowlingPoints + 10
            if strike == "true":
                bowlingPoints = bowlingPoints + 10
                strike = "false"
                spare = "false"
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins1
                strike = "false"
                spare = "false"
                factTrue()
        else:
            bowlingPoints = bowlingPoints + Pins7 + Pins8
            if strike == "true":
                bowlingPoints = bowlingPoints + Pins7 + Pins8
                factTrue()
            elif spare == "true":
                bowlingPoints = bowlingPoints + Pins7
                strike = "false"
                spare = "false"
                factTrue()
            else:
                strike = "false"
                spare = "false"
                factTrue()
    roundCount()
print(bowlingPoints)
#program that allows user to choose between three options by pressing a number key
userInput = input("Please select an option between one to three: ")
if userInput == "1" or userInput == "2" or userInput == "3":
    print(f"Option {userInput} selected")
else:
    print("Invalid option selected")
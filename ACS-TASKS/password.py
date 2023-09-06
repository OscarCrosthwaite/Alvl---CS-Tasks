#program that checks if a word is longer than eight seconds
password = input("Please input a password: ")
if len(password) > 8: 
    print("This is a valid password")
else:
    print("This is not a valid password")
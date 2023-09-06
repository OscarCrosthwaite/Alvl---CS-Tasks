userNumber = int(input("Please input a three digit number:"))
hundreds = userNumber//100
tens = (userNumber - (userNumber//100)*100)//10
digits = userNumber%10
print(f"You have {hundreds} hundreds with {tens} tens and {digits} digits. ")
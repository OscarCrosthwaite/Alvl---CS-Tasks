#program that takes a three digit number and displays it in hundreds, tens, and ones, 
userNumber = int(input("Please input a three digit number:"))
#inputs number
hundreds = userNumber//100
#finds hundreds
tens = (userNumber - (userNumber//100)*100)//10
#finds tens
digits = userNumber%10
#finds individual digits
print(f"You have {hundreds} hundreds with {tens} tens and {digits} digits. ")
#prints using format
#program that finds the total seconds from a user number of hours, minutes and seconds
hours = int(input("hours: "))
minutes = int(input("minutes: "))
seconds = int(input("seconds: "))
#finds total seconds, minutes and hours
totalSeconds = seconds + (minutes * 60) + (hours * 360)
#multiplies to find total seconds
print(totalSeconds)
#prints

print("Welcome to the tip calculator")
userInputBill = int(input("What was the total bill? "))
tipPerc = int(input("What percentage tip would you like to give?10,12 or 15? "))
noOfPeople = int(input("Number of people to split the bill "))
finalBill = (userInputBill + (userInputBill * (tipPerc/100))) / noOfPeople
print("Each Person should pay: " +str(finalBill))
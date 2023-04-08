import random
userInput = input("Enter the names, seperated by comma :\n")
userList = userInput.split(",")
randomNo = random.randint(0, len(userList)-1)
print(f"{userList[randomNo]} will pay the bill today!")
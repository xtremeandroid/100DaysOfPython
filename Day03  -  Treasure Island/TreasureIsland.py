print("Welcome to Treasure Island. Your mission is to find the treasure.")
userInput = input("you want to go left or right : \n")
if userInput == "left":
    userInput = input("will you swim or wait : \n")
    if userInput == "swim":
        print("Game Over")
    else:
        userInput = input("Which Door? red, blue or yellow? : \n")
        if userInput == "yellow":
            print("You Win !")
        else:
            print("Game Over.")
else:
    print("Game Over.")


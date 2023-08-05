from art import logo,vs
from gameData import data
import os

print(logo)
shouldContinue = True
score = 0
flag = True

def randomUser():
    from random import choice
    return choice(data)

def moreFollowers(user1,user2):
    if user1["follower_count"] > user2["follower_count"]:
        return "A"
    elif user1["follower_count"] < user2["follower_count"]:
        return "B"
    else:
        return "DRAW"

def askUser():
    global flag
    global score

    while flag:
        user1 = randomUser()
        user2 = randomUser()
        print(f"Compare A : {user1['name']}, a {user1['description']}, from {user1['country']}")
        print(vs)
        print(f"Against B : {user2['name']}, a {user2['description']}, from {user2['country']}")
        userInput = input("Who has more followers? Type 'A' or 'B': ")
        followerData = moreFollowers(user1,user2)
        if followerData != "DRAW":
            if userInput == followerData:
                score += 1
                os.system("clear")
                print(f"Current Score : {score} ")
                askUser()
            else:
                print(f"Wrong answer, your total score was {score} ")
                flag = False
        else :
            print("Seems they both have same number of followers, so we will continue with the next question.")
            os.system("clear")
            print(f"Current Score : {score} ")
            askUser()
            
askUser()






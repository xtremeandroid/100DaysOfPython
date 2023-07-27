import os
from art import logo
print(logo)
print("Welcome to Blind Auction!")

bidders = []
inputContinue = True

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def addBidderData(name,amount):
    newData = {}
    newData["Bidder Name"] = name
    newData["Bid Amount"] = amount
    bidders.append(newData)

def findMaxBidder():
    maxBidAmount =  0
    indexOfWinner = 0
    for i in range (0, len(bidders)):
        if bidders[i]["Bid Amount"] > maxBidAmount:
                maxBidAmount = bidders[i]["Bid Amount"]
                indexOfWinner = i
    bidWinner = bidders[indexOfWinner]["Bidder Name"]
    bidWinnerAmount = bidders[indexOfWinner]["Bid Amount"]
    print(f"The winner is {bidWinner} with a bid of {bidWinnerAmount}$.")

while inputContinue:
    bidderName = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    userChoice = input("Are there any other bidders? type 'yes' else type 'no'.").lower()
    addBidderData(bidderName,bid)
    cls()
    if userChoice == "no":
        findMaxBidder()
        inputContinue = False


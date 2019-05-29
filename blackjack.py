
from random import shuffle
import time


def blackjackGame(startMoney, bet):

    money = startMoney
    bet = bet
    gameStart = True
    print("Your bets are: " + str(bet) + " and you're starting with: " + str(money))
    while gameStart and money >= bet:
        gamePlay = True
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        cards = cards * 4

        shuffle(cards)
        print("Your current balance is: " + str(money) + "\n")
        money = money - bet

        userCards = 0
        dealerCards = 0

        card1 = cards.pop()
        card2 = cards.pop()
        card3 = cards.pop()
        card4 = cards.pop()

        userCards = card1 + card3
        dealerCards = card2

        print("Dealers hand is: " + str(dealerCards))
        print("Your hand is: " + str(userCards) + "\n")


        while gamePlay and userCards < 21:

            hitOrNot = input("Y for hit.. N for stick")
            time.sleep(0.5)
            if hitOrNot == "Y" or hitOrNot == "y":
                nextCard = cards.pop()

                if nextCard == 11 and userCards > 10:
                    nextCard = 1
                print("The card drawn is: " + str(nextCard))
                userCards = userCards + nextCard
                print("Your hand is: " + str(userCards) + "\n")

            elif hitOrNot == "n" or hitOrNot == "N":
                gamePlay = False
                dealerCards = dealerCards + card4
                print("Dealers hand: " + str(dealerCards))
                while dealerCards < 17:
                    nextCard = cards.pop()
                    dealerCards = dealerCards + nextCard
                    print("Dealers Hand: " + str(dealerCards))

        if userCards == 21:
            print("Blackjack! \n")

            money = money + (bet * 3)
        elif userCards > 21:
            print("Bust! \n")

        elif dealerCards > 21:
            print("You Win! \n")

            money = money + (bet * 2)
        elif userCards > dealerCards:
            print("You Win! \n")

            money = money + (bet * 2)
        elif dealerCards > userCards:
            print("You Lose! \n")


        elif dealerCards == userCards:
            print("Push! \n")

            money = money + bet

        print("\nCollecting cards and starting a new hand...")
        time.sleep(2)

        if money < bet or money < 0:
            print("You don't have enough money to play")


userMoney = int(input("please input the amount of money you would like to start with: "))
userBet = int(input("please enter the bet you would like it place each hand: "))

blackjackGame(userMoney, userBet)
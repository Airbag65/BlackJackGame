import random
from time import sleep as z

"""
TODO Deck of cards
TODO Dealer's cards are secret til' end of round
TODO Player knows their cards
TODO Card value
TODO Detect which card has been drawn
TODO     decrease chance of getting same card again
TODO Hit or stay function
TODO if over 21 == fat
TODO Choose ACE (1 or 11)
"""

deck = ["Ace", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

player_total = 0
dealer_total = 0
balance = 100


def play():
    draw_card()
    dealer()
    winning()


def draw_card():
    global player_total
    hello = input("press enter\n")
    if hello == (""):
        print("Your cards are:")
        random_card = random.randrange(12)
        print(deck[random_card])
        if random_card > 8:
            player_total += 10
        elif random_card == 0:
            player_total += 11
        else:
            player_total = player_total + random_card + 1
        z(0.5)
        print("and")
        z(0.5)
        random_card_two = random.randrange(12)
        if random_card_two > 8:
            player_total = player_total + 10
        elif random_card_two == 0:
            if random_card == 0:
                player_total = player_total + 1
            else:
                player_total = player_total + 11
        else:
            player_total = player_total + random_card_two + 1
        print(deck[random_card_two])
        print("Your total is now " + str(player_total))
        again()


def dealer():
    global dealer_total
    dealer_card = random.randrange(12)
    if dealer_card > 8:
        dealer_total += 10
    elif dealer_card == 0:
        if dealer_total + 11 > 21:
            dealer_total += 1
        else:
            dealer_total += 11
    else:
        dealer_total = dealer_card + dealer_total + 1
    dealer_card_two = random.randrange(12)
    if dealer_card_two > 8:
        dealer_total += 10
    elif dealer_card_two == 0:
        if dealer_total + 11 > 21:
            dealer_total += 1
        else:
            dealer_total += 11
    else:
        dealer_total = dealer_total + dealer_card_two + 1
    if dealer_total <= 14:
        dealer_card_three = random.randrange(12)
        if dealer_card_three > 8:
            dealer_total += 10
        elif dealer_total == 0:
            if dealer_total + 11 > 21:
                dealer_total += 1
            else:
                dealer_total += 11
        else:
            dealer_total = dealer_total + dealer_card_three + 1
    if dealer_total <= 15:
        if random.randrange(100) < 50:
            dealer_card_four = random.randrange(12)
            if dealer_card_four > 8:
                dealer_total += 10
            elif dealer_card_four == 0:
                dealer_total += 1
            else:
                dealer_total = dealer_total + dealer_card_four + 1
    print("\nDealer has a total of " + str(dealer_total))


def again():
    global player_total
    hit_or_stay = input(
        "\nType 'hit' to draw another card or type 'stay' to stop at your total of " + str(player_total) + ": ")
    if hit_or_stay == "hit":
        extra_card = random.randrange(12)
        if extra_card > 8:
            player_total += 10
            print(deck[extra_card])
            z(1)
            print("Your total is now " + str(player_total) + "!")
            if player_total < 21:
                again()
        elif extra_card == 0:
            print(deck[extra_card])
            if player_total + 11 > 21:
                player_total += 1
                z(1)
                print("Your total is now " + str(player_total) + "!")
                if player_total < 21:
                    again()
            else:
                player_total += 11
                z(1)
                print("Your total is now " + str(player_total) + "!")
                if player_total < 21:
                    again()
        else:
            print(deck[extra_card])
            player_total = player_total + extra_card + 1
            print("Your total is now " + str(player_total) + "!")
            if player_total < 21:
                again()
    elif hit_or_stay == "stay":
        print("You decided to stay at your total of " + str(player_total) + "!\n")


def winning():
    global dealer_total
    global player_total
    if dealer_total > 21:
        if player_total <= 21:
            print("\nYou Win! :)\n")
        else:
            print("\nYou are tied with the dealer\n")
    elif dealer_total <= 21:
        if player_total <= 21:
            if player_total > dealer_total:
                print("\nYou Win! :)\n")
            elif player_total == dealer_total:
                print("\nYou are tied with the dealer\n")
        elif player_total > 21:
            print("\nThe dealer beat you :(\n")


print("\nThis is a game of black jack\nThis game is nothing more than a work in progress so far.\nBetting will soon be implemented")
play_black_jack = input("Press ENTER to play \n")
if play_black_jack == "":
    play()

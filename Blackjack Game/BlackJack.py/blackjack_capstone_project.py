import random
import art

print(art)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def random_card():
    card = random.choice(cards)
    return card


bot = 0
player = 0


def user1():
    global bot
    bot = random_card()
    y_n_list = ["y", "n"]
    y_n_random = random.choice(y_n_list)
    y_n = y_n_random[0]
    if y_n == "y":
        bot += random_card()
    elif y_n == "n":
        pass
    print(f"Bot's Total sum of Cards = {bot}")


def user2():
    global player
    player = random_card()
    print(f"You got card {player}")
    y_n = input("Type [y/n] for next card: ").lower()
    if y_n == "y":
        player += random_card()
    elif y_n == "n":
        pass
    print(f"Your's Total sum of Cards = {player}")


user1()
user2()


def compare():
    global bot
    global player
    if bot > player and bot < 22:
        print("You Lost")
    elif bot < player and player < 22:
        print("You Won")


compare()

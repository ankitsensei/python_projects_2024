import os
import art
import data
import random

print(art.higher_lower)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')






def random_key(info):
    keys = info.keys()
    key = random.choice(list(info.keys()))
    return key


def values_of_keys(info, bot,  user):
    global bot_value
    global user_value
    bot_value = info[bot]
    user_value = info[user]



info = data.informations
bot_value = 0
user_value = 0
score = 0

bot = random_key(info)
while True:
    user = random_key(info)
    while user == bot:
        user = random_key(info)
    values_of_keys(info, bot, user)

    print("⭕ A.",bot)
    print(art.vs)
    print("⭕ B.",user)

    a = bot_value
    b = user_value
    try:
        ask = input("Which one is more searched? [A/B]: ").lower()
        if ask == "a":
            compare = bot_value > user_value
        elif ask == "b":
            compare = bot_value < user_value
    except ValueError:
        print("Value error")
    clear_screen()
    if compare == True:
        score+=1
        bot = user
        print(f"Your current score = {score}")
    else:
        if score == 0:
            print("A small kid would perform better than you. 🙄")
        elif score <=3:
            print("Still need improvement 😐")
        else:
            print("Umm, better I suppose 😌")
        print(f"Your total score is {score}.")
        break
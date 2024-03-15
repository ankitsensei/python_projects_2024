import os
import art
import data
import random

print(art.higher_lower)
print(art.vs)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# clear_screen()




def random_key(info):
    keys = info.keys()
    key = random.choice(list(info.keys()))
    return key



info = data.informations
while True:
    bot = random_key(info)
    user = random_key(info)
    while user == bot:
        user = random_key(info)
    print("A.",bot)
    print("B.",user)

    ask = input("Which one is more searched? [A/B]: ").upper()
    values_of_keys(info, bot, user)
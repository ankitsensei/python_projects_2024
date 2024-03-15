import os
import art


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# clear_screen()



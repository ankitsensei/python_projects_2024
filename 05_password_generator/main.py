import random

alphabets = [chr(i) for i in range(ord("a"), ord("z") + 1)] + [
    chr(i) for i in range(ord("A"), ord("Z") + 1)
]
numbers = [chr(i) for i in range(48, 58)]
symbols = [chr(i) for i in range(33, 48)]


def alpha(alphabets):
    randoms = random.choice(alphabets)
    return randoms


def num(numebrs):
    randoms = random.choice(numebrs)
    return randoms


def sym(symbols):
    randoms = random.choice(symbols)
    return randoms


def psk(psk_length):
    global random_letters
    generated_psk = ""
    for i in range(psk_length):
        random_choices = [alpha(alphabets), num(numbers), sym(symbols)]
        random_letters = random.choice(random_choices)

        generated_psk += random_letters
    return generated_psk


while True:
    print("""/// WELCOME TO PASSWORD GENERATOR ///""")
    try:
        psk_length = int(input("Please Enter the length of password you want: "))

        print("Generated password is: ")
        print(psk(psk_length))
        break
    except ValueError:
        print("Please enter length of password in numerical form.")

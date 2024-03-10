import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/MacOS
    else:
        os.system('clear')


print("Welcome to todo list")

def add_task():
    clear_terminal()
    global lst
    add = input("Enter a task: ")
    lst.append(add)
    print("SUCCESSFULLY ADDED ✅")
def delete_task():
    global lst
    count = 1
    for i in lst:
        print(count, ".", i)

def display():
    global lst
    count = 1
    for i in lst:
        print(count, ".", i)

lst = []


while True:
    print('''
✨ TODO LIST ✨
1. display ❇️
2. add task ➕
3. delete task ➖
4. task done ✅
5. task undone ❌
6. Exit ⭕
''')
    choose = int(input("SELECT ANY OPTION: "))
    if choose == 1:
        clear_terminal()
        display()
    elif choose == 2:
        clear_terminal()
        add_task()
    elif choose == 3:
        clear_terminal()
        delete_task()
    elif choose == 6:
        clear_terminal()
        break

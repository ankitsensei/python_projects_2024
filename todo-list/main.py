import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/MacOS
    else:
        os.system('clear')


print("Welcome to todo list")

def display(task):
    global lst
    count = 1
    for i in lst:
        print(f"{count}. {i}")
        count+=1
    #print completed task
    print("COMPLETED TASK ✅")
    count2 = 1
    for i in task:
        print(f"{count2}. {i}")
        count2+=1
def add_task():
    clear_terminal()
    global lst
    add = input("Enter a task: ")
    lst.append(add)
    print("ADDED SUCCESSFULLY !!!")
def delete_task():
    global lst
    count = 1
    for i in lst:
        print(count, ".", i)
        count+=1

    delete = (int(input("Enter Serial number of task to delete it: "))-1)
    try:
        # if delete>0 and delete<=len(lst):
        del lst[delete]
        print("DELETED SUCCESSFULLY !!!")
        # else:
            # print("Value out of range !!!")
    except IndexError:

        print("Value out of range.")
    except ValueError:
        print("Invalid Value.")

def task_done(task):
    global lst
    count = 1
    for i in lst:
        print(count, ".", i)
        count+=1
    ask = (int(input("Which task of your is done? : "))-1)
    try:
        task.append(ask)
        del lst[ask]
    except IndexError:
        print("Value out of range.")
    except ValueError:
        print("Invalid Value")

lst = []
task = []


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
        display(task)
    elif choose == 2:
        clear_terminal()
        add_task()
    elif choose == 3:
        clear_terminal()
        delete_task()
    elif choose == 4:
        clear_terminal()
        task_done(task)
    elif choose == 6:
        clear_terminal()
        break

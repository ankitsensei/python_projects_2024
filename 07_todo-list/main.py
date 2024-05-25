import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/MacOS
    else:
        os.system('clear')


def display(task):
    global lst
    count = 1
    print("INCOMPLETE TASKS ❌")
    if len(lst)!=0:
        for i in lst:
            print(f"{count}. {i}")
            count+=1
    else:
        print("===> NONE 😀")
    print()

    #print completed task
    print("COMPLETED TASK ✅")
    if len(task) !=0:
        count2 = 1
        for j in task:
            print(f"{count2}. {j}")
            count2+=1
    else:
        print("===> NONE 🙃")


def add_task():
    clear_terminal()
    add = input("Enter a task: ")
    lst.append(add)
    print("ADDED SUCCESSFULLY !!!")


def delete_task():
    count = 1
    for i in lst:
        print(count, ".", i)
        count+=1
    delete = (int(input("Enter Serial number of task to delete it: "))-1)
    try:
        del lst[delete]
        print("DELETED SUCCESSFULLY !!!")
    except IndexError:

        print("Value out of range.")
    except ValueError:
        print("Invalid Value.")


def task_done(task):
    count = 1
    for i in lst:
        print(count, ".", i)
        count+=1
    ask = (int(input("Which task number is done? : "))-1)
    try:
        task.append(lst[ask])
        del lst[ask]
        print("Task done 😁")
    except ValueError:
        print("Only use numbers !!")
    except IndexError:
        print("Value is out of range.")


def task_undone(task):
    count = 1
    for i in task:
        print(count, ".", i)
        count+=1
    ask = (int(input("Which task of your is undone? : "))-1)
    try:
        lst.append(task[ask])
        del task[ask]
    except IndexError:
        print("Value out of range.")
    except ValueError:
        print("Invalid Value")

lst = []
task = []

print("Welcome to todo list")
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
    try:
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
        elif choose == 5:
            clear_terminal()
            task_undone(task)
        elif choose == 6:
            clear_terminal()
            break
    except:
        print("Try again, you have to select option..")
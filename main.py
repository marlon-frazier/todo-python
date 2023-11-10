import sys


def menu():
    print("TODO APPLICATION")
    print("1) Add new task")
    print("2) Modify task")
    print("3) Delete task")
    print("4) Show all tasks")
    print("0) Exit")


def add_task():
    with open('tasks.txt', 'a') as file:
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        file.write(f"{new_task},")
        print(' ')

def modify_task():
    if len(tasks) == 0:
        print("No tasks currently; add tasks first!")
    else:
        show_all_tasks()
        modify = int(input("Which task do you want to modify? "))
        mod_task = input("What is the updated task? ")
        tasks[modify - 1] = mod_task
        with open('tasks.txt', 'w') as file:
           for task in tasks:
               file.write(f"{task},")
    print(' ')


def delete_task():
    if len(tasks) == 0:
        print("No tasks currently; add tasks first!")
    else:
        show_all_tasks()
        selected_task = int(input("Which task do you want to delete? "))
        del tasks[selected_task - 1]
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(f"{task},")

    print(' ')

def show_all_tasks():
    if len(tasks) == 0:
        print("TODO List currently empty")
    else:
        index = 1
        for item in tasks:
            if item == '':
                continue
            else:
                print(f"{index}. {item}")
                index += 1

    print(' ')

with open('tasks.txt', 'r') as file:
    content = file.read()
    tasks = content.split(',')


while True:
    menu()
    while True:
        try:
            choice = int(input("\nPlease make a selection: "))
            if choice not in range(0,5):
                print("Invalid choice")
                continue
            else:
                break
        except ValueError:
            print("Invalid choice")

    if choice == 1:
        add_task()
    elif choice == 2:
        modify_task()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        show_all_tasks()
    elif choice == 0:
        break

file.close()
sys.exit()
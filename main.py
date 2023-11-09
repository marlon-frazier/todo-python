import sys


def menu():
    print("TODO APPLICATION")
    print("1) Add new task")
    print("2) Modify task")
    print("3) Delete task")
    print("4) Show all tasks")
    print("0) Exit")


def add_task():
    new_task = input("Enter new task: ")
    tasks.append(new_task)


def modify_task():
    pass


def delete_task():
    pass


def show_all_tasks():
    print(tasks)


tasks = []


menu()
choice = int(input("\nPlease make a selection: "))
while True:
    if choice == 1:
        add_task()
        continue
    elif choice == 2:
        modify_task()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        show_all_tasks()
    elif choice == 0:
        break

sys.exit()
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
    show_all_tasks()
    modify = int(input("Which task do you want to modify? "))
    mod_task = input("What is the updated task? ")
    tasks[modify - 1] = mod_task


def delete_task():
    show_all_tasks()
    selected_task = int(input("Which task do you want to delete? "))
    del tasks[selected_task - 1]


def show_all_tasks():
    index = 1
    for item in tasks:
        print(f"{index}. {item}")
        index += 1


tasks = []


while True:
    menu()
    choice = int(input("\nPlease make a selection: "))

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

sys.exit()
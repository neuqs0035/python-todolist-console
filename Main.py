# github: neuqs534

def print_menu_header():
    print("# # # # # # # TODO LIST (GitHub: neuqs534) # # # # # # #\n")

def print_task_list(tasks):
    if not tasks:
        print("\nYour to-do list is currently empty. Let's get organized!")
    else:
        print("\n- - - - - - Tasks - - - - -\n")
        for i, task in enumerate(tasks, start=1):
            print(f"{i} > {task}", end="")
        print()

def print_options():
    print("\nOptions:")
    print("1) Add Task")
    print("2) Remove Task")
    print("3) Clear All Tasks")
    print("4) Edit Task")
    print("0) Exit")

def print_separator():
    print("\n" + "-" * 30 + "\n")

while True:
    file = open('TODO.txt', 'r')
    all_tasks = file.readlines()
    file.close()

    print_menu_header()
    print_task_list(all_tasks)
    print_options()

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nError - Invalid Input: Please enter a valid number.")
        continue

    print_separator()

    if choice == 1:
        new_task = input("\nEnter your new task: ")
        with open('TODO.txt', 'a') as file:
            file.write(new_task + "\n")
        print("\nTask added successfully! Keep it up.")

    elif choice == 2:
        task_number = int(input("\nEnter the task number to remove it: "))

        if 1 <= task_number <= len(all_tasks):
            with open('TODO.txt', 'w') as file:
                all_tasks.pop(task_number - 1)
                file.writelines(all_tasks)
            print("Task removed successfully. Great progress!")
        else:
            print("\nError: Task number is not valid. Please enter the number displayed before the task.")

    elif choice == 3:
        print("\nClear All Tasks")

        confirm = input("\nAre you sure you want to clear all tasks? (Y/N): ")

        if confirm.lower() == 'y':
            with open('TODO.txt', 'w') as file:
                file.write("")
            print('\nAll tasks cleared successfully. A fresh start!')
        elif confirm.lower() == 'n':
            print("\nClearing all tasks process canceled. Let's keep going!")
        else:
            print("\nError - Invalid Input: Enter 'Y' for Yes or 'N' for No.")

    elif choice == 4:
        task_number = int(input("\nEnter the task number you want to edit: "))

        if 1 <= task_number <= len(all_tasks):
            new_task_description = input("\nEnter the new task description: ")
            all_tasks[task_number - 1] = new_task_description

            with open("TODO.txt", "w") as file:
                file.writelines(all_tasks)

            print("Task edited successfully. Keep it updated!")

        else:
            print("\nError: Task number is not valid. Please enter the number displayed before the task.")

    elif choice == 0:
        print("\nExiting the program. Have a productive day!")
        break

    else:
        print("\nError - Invalid Input: Please check the options and enter a valid choice number.")

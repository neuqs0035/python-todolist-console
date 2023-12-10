# github : neuqs534

print("\n# # # # # # # TODO LIST (github : bhavya416) # # # # # # #\n")

while (True):

    counter = 1
    file = open('TODO.txt','r')

    all_tasks = file.readlines()
    file.close()

    if(len(all_tasks) == 0):
        print("\nList Is Empty . . . . .")

    else:
        print("\n- - - - - - Tasks - - - - -\n")
        for i in all_tasks:
            print(counter," > ",i,end="")
            counter+=1
    
    print("\n\n1 ) Add Task ")
    print("2 ) Remove Task ")
    print("3 ) Clear All Task ")
    print("4 ) Edit Task")
    print("0 ) Exit")

    choice = int(input("\n_ : "))

    if(choice == 1):

        file = open('TODO.txt','a')
        new_task = input("\nEnter Task : ")
        file.write(new_task + "\n")
        file.close()
        
        print("\nTask Added Successfully . . . . .")
    
    
    elif (choice == 2):

        file = open('TODO.txt','w')
        
        task_number = int(input("\nEnter Task Number To Remove It : "))

        if(task_number > len(all_tasks) or task_number <= 0):
            print("\nError : Task Number Is Not Valid ,  Enter The Number Displayed Before Task . . . . .")

        else:

            all_tasks.pop(task_number - 1)
            file.writelines(all_tasks)

            print("Task Removed Successfully . . . . .")
        file.close()

    elif (choice == 3):

        print("\nClear All Tasks")

        confirm = input("\nDo You Wanna Clear All Tasks ? 'Y' or 'n' : ")

        if(confirm.lower() == 'y'):

            file = open('TODO.txt','w')
            file.write("")
            file.close()
            print('\nAll Tasks Cleared Successfully . . . . .')
        
        elif(confirm.lower() == 'n'):

            print("\nClearing All Tasks Process Canceled . . . . .")
        
        else:

            print("\nError - Invalid Input : Enter 'Y' For Yes OR 'n' For No . . . . .")
    elif (choice == 4):

        print("\nEdit Task")

        task_number = int(input("\nEnter Task Number You Want To Edit : "))

        if(task_number > len(all_tasks) or task_number <= 0):
            print("\nError : Task Number Is Not Valid ,  Enter The Number Displayed Before Task . . . . .")

        else:
            new_task_description = input("\nEnter New Task Description : ")
            all_tasks[task_number-1] = new_task_description

            file = open("TODO.txt","w")
            file.writelines(all_tasks)
            file.close()


    elif (choice == 0):

        print("\nProgram Exited . . . . .")
        break

    else:
        print("\nError - Invalid Input : Please Check Option And Enter Valind Choice Number")

# github : bhavya416
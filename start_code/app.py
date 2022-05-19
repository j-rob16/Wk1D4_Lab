from modules.task_list import *
from modules.output import *
from modules.Data.task_list import *
from modules.input import *

while True:
    print_menu()
    option = select_option()
    # option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    if option.lower() == "q":
        break
    if option == "1":
        print_list(tasks)
    elif option == "2":
        print_list(get_uncompleted_tasks(tasks))
    elif option == "3":
        print_list(get_completed_tasks(tasks))
    elif option == "4":
        description = select_description()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == "5":
        time = select_duration()
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == "6":
        description = select_description()
        print(get_task_with_description(tasks, description))
    elif option == "7":
        description = select_description()
        time_taken = select_duration()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")

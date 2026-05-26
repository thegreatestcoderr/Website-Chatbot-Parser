to_do_list = []
def add_task(task):
    to_do_list.append(task)
    print(task + " added to your to - do list.")
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        to_do_list.remove(task + " completed.")
    else:
        print("Task not found.")
def mark_task(task, mark):
    if task in to_do_list:
        to_do_list.append(task + mark)
        print("Your task has been marked.")
    else:
        print("Task not found.")
def view_list():
    if not to_do_list:
        print("Your to - do list is empty.")
    else:
        print("Your to - do list is:")
        for task in to_do_list:
            print("- " + task)
try:
    while True:
        print("Your to - do list menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as completed")
        print("4. View list")
        print("5. Quit")
        choice = input("What do you want to do? (Enter number of choice):")
        if choice == "1":
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task you want to remove: ")
            remove_task(task)
        elif choice == "3":
            task = input("Enter the task you want to mark: ")
            mark = input("Enter the number of the mark you want (3.1: Mark as completed, 3.2: Mark as paused, 3.3: resume): ")
            if input == "3.1":
                mark_task(task, "completed")
            elif input == "3.2":
                mark_task(task, "paused")
                
        elif choice == "4":
            view_list()
        elif choice == "5":
        
            break
        else:
            print("Invalid choice. Please enter the number of the action you wish to take.")
except:
    print("Invalid input. Please retry.")

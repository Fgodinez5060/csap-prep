# Prompt for number of tasks in list
number_of_tasks = input("How many tasks did you work on today? ")

try:
    # Convert number from string to int and initialize tasks list
    number_of_tasks = int(number_of_tasks)
    tasks = []

    # Fill list with names from user input
    for i in range(number_of_tasks):
        task = input(f"Enter task #{i+1} ")
        tasks.append(task)
    
    # Print list
    print("You worked on:")
    for task in tasks:
        print(f"    - {task}")
        
    # Prompt for removal of item in list
    edit = input("Do you want to remove any tasks from the list? (yes/no) ").lower().strip()
    # Prompt for which task is to be removed and remove it
    if edit == "yes":
        removed = input("What is the exact name of the task you'd like to remove? ").strip()
        if removed in tasks:
            tasks.remove(removed)
        else:
            print("That task wasn't in your list")
        
        # Print updated list
        print("Updated list:")
        for task in tasks:
            print(f"    - {task}")

    # End program with a print statement
    elif edit == "no":
        print("All tasks saved. Good work!")

except ValueError:
    print("Please enter a proper value")
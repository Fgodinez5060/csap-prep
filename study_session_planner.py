# Initialize study_log dictionary
study_log = {
    "Monday": 0.0,
    "Tuesday": 0.0,
    "Wednesday": 0.0,
    "Thursday": 0.0,
    "Friday": 0.0,
}

# Function to get a 'yes' or 'no' from user with any given prompt
def get_yes_or_no(prompt):
    answer = input(f"{prompt}, please answer 'yes' or 'no'. ").lower().strip()
    if answer == "yes":
        return answer
    elif answer == "no":
        return answer
    else:
        print("Invalid response. Please type 'yes' or 'no'. ")
        return get_yes_or_no(prompt)

# Function to get number of hours studied from user on any given day
def get_study_hours(day):
    result = input(f"How many hours did you study on {day}? ")
    try:
        result = float(result)
        return result

    except ValueError:
        print("Invalid response. Please enter a valid number")
        return get_study_hours(day)

# Function to print summary of days and hours studied from dictionary as well as calculating and printing total_hours
def print_summary(study_log):
    total_hours = 0.0
    for day, hours in study_log.items():
        total_hours += hours
        print(f"{day}: {hours:.1f} hours")
    print(f"Total hours studied: {total_hours:.1f}")

    if total_hours >= 10:
        print("Great job staying focused this week!")

    elif 5 <= total_hours < 10:
        print("Solid effort, keep building the habit.")

    elif total_hours < 5:
        print("Let's try to dedicate more time next week.")

# Function to save the study log with a choice of overwriting or appending to the txt file
def save_study_log(log_dict):
    total_hours = 0.0
    while True:
        choice = input("Would you like to save as an overwrite or append? (Please reply with 'over' or 'app') ").lower().strip()
        
        if choice == "over":
            with open("study_log.txt", "w") as file:
                for day, hours in log_dict.items():
                    file.write(f"{day}: {hours:.1f} hours\n")
                    total_hours += hours
                file.write(f"Total: {total_hours:.1f} hours\n")
            break

        elif choice == "app":
            with open("study_log.txt", "a") as file:
                for day, hours in log_dict.items():
                    file.write(f"{day}: {hours:.1f} hours\n")
                    total_hours += hours
                file.write(f"Total: {total_hours:.1f} hours\n")
            break

        else:
            print("Invalid response. Please enter a valid option ('over' or 'app')")

# Function to open text file and see if there is recprevious study log data to print
def load_study_log():
        try:
            with open("study_log.txt", "r") as file:
                print("Previous Study Log:")
                for line in file:
                    print(line.strip())
                print("")
        except FileNotFoundError:
            print("No previous study log found")


# Calls function to load previous study log if available
load_study_log()

# Main loop to get hours studied on specific days from user
for day in study_log:
    result = get_yes_or_no(f"Did you study on {day}?")
    if result == "yes":
        hours_studied = get_study_hours(day)
        study_log[day] = hours_studied
    
    elif result == "no":
        study_log[day] = 0

# Call function to display final summary
print_summary(study_log)

save_study_log(study_log)
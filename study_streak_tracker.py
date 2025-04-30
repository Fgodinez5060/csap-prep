
# Initialize new dictionary with weekdays and no string by default
weekdays = {
    "Monday": "no",
    "Tuesday": "no",
    "Wednesday": "no",
    "Thursday": "no",
    "Friday": "no"
}

daysStudied = 0

# Loop through all items in weekdays dictionary
for day in weekdays:

    # Ask if they have studied on a certain day
    study = input(f"Did you study on {day}? (y/n)").lower().strip()

    # If they reply with yes, update that days value to yes
    if study == "y":
        weekdays[day] = "yes"
        daysStudied += 1

    # If they reply with no, update that days value to no
    # (It is already false but for attention to detail I will be updating it to no anyway)
    elif study == "n":
        weekdays[day] = "no"

    else:
        print("Invalid response. Please type 'y' or 'n'.")

# Spacer for cleaner output
print("")

# Output string based on performance
if daysStudied == 5:
    print("Perfect streak! Keep it up!\n")

elif 2 < daysStudied < 5:
    print("Solid week! You're building momentum.\n")

else:
    print("Let's aim for more consistency next week.\n")

# Finally print list
print("Study log:")
for day, result in weekdays.items():
    print(f"{day}: {result}")
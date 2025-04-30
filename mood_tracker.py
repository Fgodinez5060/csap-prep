# Initialize new dictionary and populate variables
days = {
    "Monday": "",
    "Tuesday": "",
    "Wednesday": ""
}

# Loop to get mood from user for every day in days dictionary
for day, mood in days.items():
    mood = input(f"Enter your mood for {day}: ")
    days[day] = mood

# Print back updated dictionary with user inputed values
print("Your mood this week:")
for day, mood in days.items():
    print(f"{day}: {mood}")
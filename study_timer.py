import time

print("Welcome to the Study Timer!")
minutes = input("How many minutes would you like to study for? ")

# Validate input
try:
    minutes = int(minutes)
    print(f"Starting a {minutes}-minute study session...")

    for i in range(minutes):
        print(f"Minute {i+1} of {minutes}")
        time.sleep(1)

    response = input("Do you want to take a 5-minute break? (yes/no) ").lower()
    if response == "yes":
        for i in range(5):
            print(f"Minute {i+1} of 5")
            time.sleep(1)
        print("Break over. Time to get back to work!")

    elif response == "no":
        print("Okay, session complete. Nice work!")

    else:
        print("Improper response.")

except ValueError:
    print("Please enter a valid number.")
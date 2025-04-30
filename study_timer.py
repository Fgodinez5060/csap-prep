import time

print("Welcome to the Study Timer!")
minutes = input("How many minutes would you like to study for? ")

# Validate input
try:
    minutes = int(minutes)
    print(f"Starting a {minutes}-minute study session...")

    for i in range(minutes):
        print(f"minute {i+1} of {minutes}")
        time.sleep(1)

    print("Study session over! Time for a break")

except ValueError:
    print("Please enter a valid number.")
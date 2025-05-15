from datetime import datetime, timedelta

class HabitTracker:
    def __init__(self):
        # Initialize an internal list of habits
        # Load existing habits from the file (if it exists)

        self.habits = []
        self.load_from_file()

    def add_habit(self):
        # Ask the user for a habit name
        # Add it to the list with a streak of 0 and today's date

        habit_name = input("What is the name of the new habit? ").strip()

        for habit in self.habits:
            if habit["name"].lower() == habit_name.lower():
                print("That habit already exists!")
                return
            
        today = datetime.today().strftime("%Y-%m-%d")
        self.habits.append({
                "name": habit_name,
                "streak": 0,
                "last_updated": today
        })
        print(f"habit '{habit_name}' added.")

    def check_in(self):
        # Go through each habit one by one
        # Ask the user if they completed it today (y/n)
        # If completed today and date is different → increment streak and update date
        # If skipped (or missed a day) → reset streak and update date

        today = datetime.today().date()  # today's date as a date object
        yesterday = today - timedelta(days=1)

        for habit in self.habits:
            last_updated = datetime.strptime(habit["last_updated"], "%Y-%m-%d").date()

            completed = input(f"Have you completed the habit '{habit['name']}' today? (y/n) ").lower().strip()

            if completed == "y":
                if last_updated == today:
                    print(f"You've already logged '{habit['name']}' today.")
                elif last_updated == yesterday:
                    habit["streak"] += 1
                    habit["last_updated"] = today.strftime("%Y-%m-%d")
                    print(f"Nice! Streak for '{habit['name']}' is now {habit['streak']} days.")
                else:
                    habit["streak"] = 1
                    habit["last_updated"] = today.strftime("%Y-%m-%d")
                    print(f"Restarted streak for '{habit['name']}' at 1 day.")
        
            elif completed == "n":
                habit["streak"] = 0
                habit["last_updated"] = today.strftime("%Y-%m-%d")
                print(f"Streak for '{habit['name']}' reset to 0.")

            else:
                print("Invalid input. Please type 'y' or 'n'.")
            

    def show_streaks(self):
        # Print each habit and its current streak count to the console

        for habit in self.habits:
            print(f"{habit['name']}: {habit['streak']} day streak (Last updated: {habit['last_updated']})")

    def save_to_file(self):
        # Save all habits (name, streak, last updated date) to a txt file

        try:
            with open ("habit_data.txt", "w") as file:
                for habit in self.habits:
                    file.write(f"{habit['name']},{habit['streak']},{habit['last_updated']}\n")

        except FileNotFoundError:
            print("File could not be found.")

    def load_from_file(self):
        # Read the habits file and reconstruct the habit list in memory
        # Each habit line includes: name, streak count, last updated date

        with open ("habit_data.txt", "r") as file:
            for line in file:
                line = line.strip()
                name, streak, date = line.split(",")
                streak = int(streak)

                self.habits.append({
                    "name": name,
                    "streak": streak,
                    "last_updated": date
                })

tracker = HabitTracker()

while True:
    print("==== Habit Tracker Menu ====")
    print("1. Add Habit")
    print("2. Check In")
    print("3. Show Streaks")
    print("4. Save and Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        tracker.add_habit()
    elif choice == "2":
        tracker.check_in()
    elif choice == "3":
        tracker.show_streaks()
    elif choice == "4":
        tracker.save_to_file()
        print("Habits saved. Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-4.")
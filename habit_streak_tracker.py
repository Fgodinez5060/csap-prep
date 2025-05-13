class HabitTracker:
    def __init__(self):
        # Initialize an internal list of habits
        # Load existing habits from the file (if it exists)
        pass

    def add_habit(self):
        # Ask the user for a habit name
        # Add it to the list with a streak of 0 and today's date
        pass

    def check_in(self):
        # Go through each habit one by one
        # Ask the user if they completed it today (y/n)
        # If completed today and date is different → increment streak and update date
        # If skipped (or missed a day) → reset streak and update date
        pass

    def show_streaks(self):
        # Print each habit and its current streak count to the console
        pass

    def save_to_file(self):
        # Save all habits (name, streak, last updated date) to a txt file
        pass

    def load_from_file(self):
        # Read the habits file and reconstruct the habit list in memory
        # Each habit line includes: name, streak count, last updated date
        pass
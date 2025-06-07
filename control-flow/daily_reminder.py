# daily_reminder.py

# Prompt user for task input
task = input("Enter your task: ")

# Loop until a valid priority is given
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Please enter a valid priority: high, medium, or low.")

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Plan to work on it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")



## User Prompt for a daily reminder
task = input("Enter your task: ")
priority = input("(high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

## Match case based on task's priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' invalid priority input."
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += f". Consider completing it when you have free time."

## Output
print("\n" + message)

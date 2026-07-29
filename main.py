import todo

options = ["1", "2", "3"]
task = todo.Task()

while True:
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. Exit")

    choice = input("Enter menu choice: ")

    if choice == "1":
        date = input("Enter date task must be completed by (YYYY-MM-DD): ")
        if task.checkDate(date):
            time = input("Enter what time the task must be completed by (HH:MM): ")
            if task.checkTime(time):
                desc = input("Enter task description: ")
                task.setTask(date, desc, time)
            else:
                print("Invalid time format. Please use HH:MM.")
                continue
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
    elif choice == "2":
        date = input("Enter the date of the task to mark as completed (YYYY-MM-DD): ")
        if task.checkDate(date):
            if date in task.task:
                time = input("Enter the time of the task to mark as completed (HH:MM): ")
                if task.checkTime(time):
                    task.taskdone(date, time)
                elif time not in task.task[date]:
                    print(f"No task found for {date} at {time}.")
            else:
                print(f"No task found for {date}.")
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
    elif choice == "3":
        print("Thank you for using the task manager, please come again :).")
        break

    if choice not in options:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue
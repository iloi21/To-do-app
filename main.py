import todo

options = ["1", "2", "3", "4", "5", "6", "7"]
task = todo.Task()

while True:
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Mark a task as completed")
    print("4. Show number of flowers earned")
    print("5. Delete a task")
    print("6. Reschedule a task")
    print("7. Exit")

    choice = input("Enter menu choice: ")

    if choice == "1":
        date = input("Enter date task must be completed by (YYYY-MM-DD): ")
        if task.checkDate(date):
            time = input("Enter what time the task must be completed by (HH:MM AM/PM): ")
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
        task.showTask()
    elif choice == "3":
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
    elif choice == "4":
        task.checkFlowers()
    elif choice == "5":
        date = input("Enter the date of the task to delete (YYYY-MM-DD): ")
        if task.checkDate(date):
            if date in task.task:
                time = input("Enter the time of the task to delete (HH:MM): ")
                if task.checkTime(time):
                    task.deleteTask(date, time)
                elif time not in task.task[date]:
                    print(f"No task found for {date} at {time}.")
            else:
                print(f"No task found for {date}.")
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
    elif choice == "6":
        date = input("Enter the date of the task to reschedule (YYYY-MM-DD): ")
        if task.checkDate(date):
            if date in task.task:
                time = input("Enter the time of the task to reschedule (HH:MM): ")
                if task.checkTime(time):
                    new_date = input("Enter the new date for the task (YYYY-MM-DD): ")
                    if task.checkDate(new_date):
                        new_time = input("Enter the new time for the task (HH:MM AM/PM): ")
                        if task.checkTime(new_time):
                            task.rescheduleTask(date, time, new_date, new_time)
                        else:
                            print("Invalid new time format. Please use HH:MM AM/PM.")
                    else:
                        print("Invalid new date format. Please use YYYY-MM-DD.")
                elif time not in task.task[date]:
                    print(f"No task found for {date} at {time}.")
            else:
                print(f"No task found for {date}.")
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
    elif choice == "7":
        print("Thank you for using the task manager, please come again :).")
        break

    if choice not in options:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")
        continue
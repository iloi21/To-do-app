import todo

options = ["1", "2"]

while True:
    print("1. Add a new task")
    print("2. Exit")

    choice = input("Enter menu choice: ")

    if choice == "1":
        date = input("Enter date task must be completed by (YYYY-MM-DD): ")
        if todo.checkDate(date):
            time = input("Enter what time the task must be completed by (HH:MM): ")
            if todo.checkTime(time):
                todo.setDate(date, time)
                info = input("Enter task information: ")
                # figure out how to store the task information with the date and time
            else:
                print("Invalid time format. Please use HH:MM.")
                continue
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
    elif choice == "2":
        print("Exiting the program.")
        break

    if choice not in options:
        print("Invalid choice. Please enter 1 or 2.")
        continue
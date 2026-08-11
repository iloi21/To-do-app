import os
import sys
from datetime import datetime

class Task:
    def __init__(self):
        # For storing tasks (date is key, value is a dictionary where time is key and description is value)
        self.task = {}
        # Counter for flowers (reward system)
        self.flowers = 0

# Helper functions that check for stuff
    def checktask(self): # This function needs to be used in main
        # checking if there are any tasks in the system
        try:
            self.task
        except AttributeError:
            return False
        
        

    def checkDate(self, date):
        # checking if date is valid
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def checkTime(self, time):
        # checking if time is valid
        try:
            datetime.strptime(time, '%H:%M %p')
            return True
        except ValueError:
            return False

    # Main functions that help with tasks

    def setTask(self, date, desc, time):
        # will not move on if the date or time is invalid, and will print an error message
        if not self.checkDate(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        if not self.checkTime(time):
            print("Invalid time format. Please use HH:MM.")
            return

        time24 = datetime.strptime(time, '%I:%M %p').strftime('%H:%M')
        # adds new date if it's not already in the system
        if date not in self.task:
            self.task[date] = {}
        # adds the time and description of the task
        self.task[date][time] = {"description": desc}
        # confirmation that task has been added to system
        print(f"Task set for {date} at {time}: {desc}")

    def taskdone(self, date, time):    
        # checking if date and time are valid to mark the task as completed
        # will not move on if the date or time is invalid, and will print an error message
        if not self.checkDate(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        if not self.checkTime(time):
                print("Invalid time format. Please use HH:MM.")
                return
        # will mark task as completed if date and time are valid, and will print a confirmation message
        if date in self.task and time in self.task[date]:
            del self.task[date][time]
            if not self.task[date]:  # If no tasks left for the date, remove the date entry
                del self.task[date]
                print(f"Task for {date} at {time} marked as completed.")
                # gives reward after marking task as completed, and will print a confirmation message
                print("You have earned a flower for completing a task!")
                self.flowers += 1
            else:
                # If the date or time is not found in the system, it will say that it wasn't
                print(f"No task found for {date} at {time}.")
    

    def showTask(self):
        # displays all tasks in the system, sorted by date and time

        for date in sorted(self.task.keys()):
            print(f"Tasks for {date}:")
            for time in sorted(self.task[date].keys()):
                desc = self.task[date][time]["description"]
                print(f"  {time} - {desc}")
    
    def deleteTask(self, date, time):
       # deletes key from dictionary (along with value) if date and time are valid, and will print a confirmation message
        if not self.checkDate(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        if not self.checkTime(time):
            print("Invalid time format. Please use HH:MM.")
            return
        if date in self.task and time in self.task[date]:
            del self.task[date][time]
            if not self.task[date]:  # If no tasks left for the date, remove the date entry
                del self.task[date]
            print(f"Task for {date} at {time} deleted.")
            print(f"Deleting tasks do not earn you a flower, but you can always add a new task to earn one!")
        else:
            print(f"No task found for {date} at {time}.")

    def rescheduleTask(self, date, time, new_date, new_time):
        # If date and time = valid, reschedule
        if date in self.task and time in self.task[date]:
            desc = self.task[date][time]["description"] # keeps description in temp var
            del self.task[date][time] # deletes old date and time
            if not self.task[date]:  # If no tasks left for the date, remove the date entry
                del self.task[date]
            self.setTask(new_date, desc, new_time) # sets new time and date with old description
            print(f"Task rescheduled from {date} at {time} to {new_date} at {new_time}.")

    # reward system for completing tasks

    def checkFlowers(self):
        # allows user to check how many flowers they have earned, and will print a message based on the number of flowers earned
        if self.flowers < 10:
            print(f"You have {self.flowers} flowers. Keep completing tasks to earn a bouquet!")
        elif self.flowers == 10:
            print("Great job! you have 10 flowers! You made yourself a bouquet! Keep earning more to create a garden (20+ flowers)! XD")
        elif self.flowers == 20:
            print("Wow! you have 20 flowers! You made yourself a garden! Keep earning more to create a field (50+ flowers)! XD")
        elif self.flowers >= 50:
            print(f"Amazing! you have {self.flowers} flowers! You made yourself a field! Keep earning more to create a forest (100+ flowers)! XD")

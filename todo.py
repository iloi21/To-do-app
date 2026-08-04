import os
import sys
from datetime import datetime

class Task:
    def __init__(self):
        self.task = {}
        self.flowers = 0

    def checkDate(self, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def checkTime(self, time):
        try:
            datetime.strptime(time, '%H:%M %p')
            return True
        except ValueError:
            return False

    def setTask(self, date, desc, time):
        
        if not self.checkDate(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        if not self.checkTime(time):
            print("Invalid time format. Please use HH:MM.")
            return

        time24 = datetime.strptime(time, '%I:%M %p').strftime('%H:%M')

        if date not in self.task:
            self.task[date] = {}

        self.task[date][time] = {"description": desc}

        print(f"Task set for {date} at {time}: {desc}")

    def taskdone(self, date, time):
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
            print(f"Task for {date} at {time} marked as completed.")
            print("You have earned a flower for completing a task!")
            self.flowers += 1
        else:
            print(f"No task found for {date} at {time}.")

    def showTask(self):
        if not self.task:
            print("No tasks available.")
            return

        for date in sorted(self.task.keys()):
            print(f"Tasks for {date}:")
            for time in sorted(self.task[date].keys()):
                desc = self.task[date][time]["description"]
                print(f"  {time} - {desc}")

    def checkFlowers(self):
        if self.flowers < 10:
            print(f"You have {self.flowers} flowers. Keep completing tasks to earn more!")
        elif self.flowers == 10:
            print("Great job! you have 10 flowers! You made yourself a bouquet! Keep earning more to create a garden (20+ flowers)! XD")
        elif self.flowers == 20:
            print("Wow! you have 20 flowers! You made yourself a garden! Keep earning more to create a field (50+ flowers)! XD")
        elif self.flowers >= 50:
            print(f"Amazing! you have {self.flowers} flowers! You made yourself a field! Keep earning more to create a forest (100+ flowers)! XD")

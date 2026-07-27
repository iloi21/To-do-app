import os
import sys
from datetime import datetime

class task:
    def __init__(self):
        self.task = {}

    def checkDate(self, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def checkTime(self, time):
        try:
            datetime.strptime(time, '%H:%M')
            return True
        except ValueError:
            return False

    def setDate(self, date, info):
        if self.checkDate(date):
            self.task[date] = info
            print(f"Task added: {info} (Due by: {date})")
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")
        


    
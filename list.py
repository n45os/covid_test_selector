from person import Person
import settings
import pandas as pd
import csv
import get_history
import datetime
import datetime


class List:

    def __init__(self):
        self.date = datetime.date.today()
        self.number = get_history.times_used + 1
        self.people_list = []
        self.prev_list_date = get_history.last_used

    def add_chosen(self, person: Person):
        self.people_list.append(person)

    def id_in_list(self, id):
        for p in self.people_list:
            if p.id == id:
                return True
        return False

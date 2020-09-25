import calendar
import datetime
import settings


class Person:
    def __init__(self, id, name, points, time_mul, times_choosen, last_choosen,
                 currently_choosen, relativeness, previously_chosen):
        self.id = id
        self.name = name
        self.points = points
        self.time_mul = time_mul
        self.times_chosen = times_choosen
        self.last_chosen = last_choosen
        self.currently_chosen = currently_choosen
        self.relativeness = relativeness
        self.previously_chosen = previously_chosen

    def update_data(self, p_list):
        if p_list.id_in_list(self.id):
            self.currently_chosen = settings.TIMES_W_NO_CHANCE
            self.time_mul = 0
            self.previously_chosen = self.last_chosen
            self.last_chosen = p_list.date
            self.times_chosen += 1
        else:
            if self.currently_chosen == 0 and self.time_mul < 1:
                self.time_mul += settings.TIME_MUL_PER_PASSING_TEST
                if self.time_mul > 1:
                    self.time_mul = 1
            elif self.currently_chosen > 0:
                self.currently_chosen -= 1


"""
cointains the list of the stuff
"""


class People:
    people_array = []

    def __init__(self):
        super().__init__()

    def add_people(self, p: Person):
        self.people_array.append(p)

    def update_people(self, p_list):
        for p in self.people_array:
            p.update_data(p_list)
        print("Data History updated.")

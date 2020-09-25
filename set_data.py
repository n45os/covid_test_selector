import pandas as pd
from list import List
from person import Person, People
import get_data
import get_history
import settings
import csv

def update_storage(t_list, pple):
    store_data(t_list, pple)
    print("New data history was stored.")
    store_list(t_list)
    print("People list was stored.")
    update_state(t_list)
    print("State updated.")

def store_data(t_list, pple):
    new_data_csv_file = "{}/Data History/dhNo{} on {}.csv".format(settings.DIR, t_list.number, t_list.date)
    header = ("id", "name", "points", "relativeness", "time_mul","times_chosen",
              "last_chosen", "currently_chosen","previously_chosen")

    with open(new_data_csv_file, "w") as history_file:
        writer = csv.writer(history_file)
        writer.writerow(header)
        for person in pple.people_array:
            data = [person.id, person.name, person.points, person.relativeness, person.time_mul, person.times_chosen,
                    person.last_chosen, person.currently_chosen, person.previously_chosen]
            writer.writerow(data)
        history_file.close()

def store_list(t_list):
    new_list_csv_file = "{}/Outputs/TestingNo{} on {}.csv".format(settings.DIR, t_list.number, t_list.date)
    header = ("Name", "Last time chosen")
    with open(new_list_csv_file, "w") as history_file:
        writer = csv.writer(history_file)
        writer.writerow(["Date:", t_list.date])
        writer.writerow(header)
        for person in t_list.people_list:
            writer.writerow([person.name, person.previously_chosen])
        history_file.close()

def update_state(t_list):
    state_file = "{}/state.csv".format(settings.DIR)
    r = csv.reader(open(state_file, "r"))
    lines = list(r)
    lines[1][0] = t_list.date
    lines[1][1] = t_list.number
    lines[1][2] = int(lines[1][2]) + 1
    lines[1][3] = "{}/Outputs/TestingNo{} on {}.csv".format(settings.DIR, t_list.number, t_list.date)
    lines[1][4] = "{}/Data History/dhNo{} on {}.csv".format(settings.DIR, t_list.number, t_list.date)
    with open(state_file, "w") as st_file:
        writer = csv.writer(st_file)
        writer.writerow(lines[0])
        writer.writerow(lines[1])
        st_file.close()

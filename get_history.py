import csv
import pandas as pd
import datetime
import settings

try:
    read_state_file = pd.read_csv(r"{}/state.csv".format(settings.DIR))
    df = pd.DataFrame(read_state_file)
    last_used = df["last_used"].values[0]
    current_list_num = df["current_list_num"].values[0]
    times_used = df["times_used"].values[0]
    last_list_file = df["last_list_file"].values[0]
    last_data_file = df["last_data_file"].values[0]
except:
    print("There was an error with the state file, check if it's directory is in proper path.")
    import sys

    sys.exit()

try:
    read_history_csv_file = pd.read_csv(r"{}/Data History/dhNo{} on {}.csv".
                                        format(settings.DIR, current_list_num, last_used))
    df = pd.DataFrame(read_history_csv_file)
    ids = df["id"].tolist()
    names = df["name"].tolist()
    points = df["points"].tolist()
    relativeness = df["relativeness"].tolist()
    time_mul = df["time_mul"].tolist()
    times_chosen = df["times_chosen"].tolist()
    last_chosen = df["last_chosen"].tolist()
    currently_chosen = df["currently_chosen"].tolist()
    previously_chosen = df["previously_chosen"].tolist()

except FileNotFoundError:
    print("First time used, initializing the data files.")
    last_used = datetime.date.today()
    current_list_num = 1
    times_used = 0
    time_mul = []
    times_chosen = []
    last_chosen = []
    currently_chosen = []
    previously_chosen = []

    header = ("id", "name", "points", "relativeness", "time_mul",
              "times_chosen", "last_chosen", "currently_chosen", "previously_chosen")
    with open(r"{}/Data History/dhNo{} on {}.csv".format(settings.DIR, current_list_num, last_used), "w") \
            as history_file:
        writer = csv.writer(history_file)
        writer.writerow(header)

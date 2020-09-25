import os
import pandas as pd
import csv

DIR = os.path.dirname((os.path.realpath(__file__)))

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def change_settings():
    while True:
        print("Press:\n"
              f"{OKBLUE}l {ENDC}to change {OKBLUE} list size\n{ENDC}"
              f"{OKBLUE}t {ENDC}to change {OKBLUE} times with no change\n{ENDC}"
              f"{OKBLUE}m {ENDC}to change {OKBLUE} multiplication per passing test\n{ENDC}"
              f"{OKBLUE}b {ENDC}to go {OKBLUE} back to the menu\n{ENDC}")
        inp = input()
        if inp == 'l':
            print(f"Type the {OKBLUE}length of the new list size{ENDC}")
            global LIST_SIZE
            LIST_SIZE = change("LIST_SIZE")
            break
        elif inp == "t":
            print(f"Type the{OKBLUE} times with no change{ENDC}")
            global TIMES_W_NO_CHANCE
            TIMES_W_NO_CHANCE = change("TIMES_W_NO_CHANCE")
            break
        elif inp == "m":
            print(f"Type the {OKBLUE}multiplication per passing test{ENDC}")
            global TIME_MUL_PER_PASSING_TEST
            TIME_MUL_PER_PASSING_TEST = change("TIME_MUL_PER_PASSING_TEST")
            break
        elif inp == "b":
            break
        else:
            print(f"{WARNING}TYPE ONE OF THE OPTIONS!{ENDC}")
            continue


def change(setting):
    while True:
        try:
            read_settings_file = open(r"{}/SETTINGS.csv".format(DIR), "r")
            read = csv.reader(read_settings_file)
            all_list = list(read)
            data = []
            header = []
            from io import StringIO
            for i in range(0, len(all_list[0])):
                data.append(all_list[1][i])
                header.append(all_list[0][i])
            index = 0
            for set in header:
                if setting == set:
                    break
                index += 1
            inp2 = input()
            data[index] = int(inp2)  # gives a ValuseError so it catches the exeption
            settings_file = open(r"{}/SETTINGS.csv".format(DIR), "w")
            writer = csv.writer(settings_file)
            writer.writerow(header)
            writer.writerow(data)
            settings_file.close()
            return int(inp2)
        except ValueError:
            print(f"{FAIL}GIVE A NUMBER{ENDC}")


read_settings = pd.read_csv(r"{}/SETTINGS.csv".
                            format(DIR))
df = pd.DataFrame(read_settings)
LIST_SIZE = df["LIST_SIZE"].values[0]
TIMES_W_NO_CHANCE = df["TIMES_W_NO_CHANCE"].values[0]
TIME_MUL_PER_PASSING_TEST = df["TIME_MUL_PER_PASSING_TEST"].values[0]

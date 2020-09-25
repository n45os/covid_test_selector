import settings
import pandas as pd
from list import List
from person import Person, People
import csv
import json


def get_data(pple):
    try:
        read_xl = pd.read_excel(r"{}/test_list.xlsx".format(settings.DIR))
        df_xl = pd.DataFrame(read_xl)
        ids = []
        names = df_xl["name"].tolist()
        id = 0
        for _ in names:
            ids.append(id)
            id += 1
        points = df_xl["points"].tolist()
        relativeness = df_xl["relativeness"].tolist()
    except Exception:
        print(f"{settings.FAIL}could not extract the data from the Excel file. "
              f"{settings.WARNING}See the {settings.BOLD}{settings.UNDERLINE}README{settings.ENDC}{settings.WARNING} "
              f"file to format it properly.")
        import sys
        sys.exit()
    print("Extracted data from Excel.")

    import get_history
    time_mul = get_history.time_mul
    times_chosen = get_history.times_chosen
    last_chosen = get_history.last_chosen
    currently_chosen = get_history.currently_chosen
    previously_chosen = get_history.previously_chosen


    while len(time_mul) < len(ids):
        time_mul.append(1)
        times_chosen.append(0)
        last_chosen.append("---")
        currently_chosen.append(0)
        previously_chosen.append("---")

    for i in range(0, len(ids)):
        p = Person(id=ids[i], name=names[i], points=points[i], time_mul=time_mul[i],
                   times_choosen=times_chosen[i],last_choosen=last_chosen[i], currently_choosen=currently_chosen[i],
                   relativeness=relativeness[i], previously_chosen=previously_chosen[i])
        pple.people_array.append(p)
    print("People list variable loaded.")

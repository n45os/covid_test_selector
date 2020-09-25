from list import List
from person import Person, People
import get_data
import settings
import set_data
import datetime


pple = People()
print("People variable created.")
l = List()  # the test list
print("Test list variable created.")
get_data.get_data(pple)



def rand_float_range(start, end):
    import random
    return random.random() * (end - start) + start


def recalculate_points():
    for person in pple.people_array:
        person.points = person.points * person.time_mul * (0 if person.currently_chosen>0 else 1)


def choosing():
    summ = 0
    recalculate_points()
    for i in range(0, len(pple.people_array)):
        summ += pple.people_array[i].points
    if summ > 0:
        while len(l.people_list) < settings.LIST_SIZE:
            chosen = rand_float_range(0, summ)
            if chosen > summ / 2:
                temp_choice = summ
                chosen_id = pple.people_array[len(pple.people_array) - 1].id
                while chosen < temp_choice:
                    temp_choice -= pple.people_array[chosen_id].points
                    chosen_id -= 1
                chosen_id += 1
            else:
                temp_choice = pple.people_array[0].points
                chosen_id = pple.people_array[0].id
                while chosen > temp_choice:
                    temp_choice += pple.people_array[chosen_id].points
                    chosen_id += 1
                chosen_id -= 1
            counter = 0
            for j in range(0, len(l.people_list)):
                if ((chosen_id != l.people_list[j].id) and
                        ((pple.people_array[chosen_id].relativeness != l.people_list[j].relativeness) or
                         (pple.people_array[chosen_id].relativeness == 0)) and
                        (len(l.people_list) < settings.LIST_SIZE)):
                    counter += 1
            if counter == len(l.people_list):
                l.people_list.append(pple.people_array[chosen_id])
                counter = 0
    else:
        print(f"{settings.FAIL}cannot execute, no one can be chosen.{settings.ENDC}")
        import sys
        sys.exit()



def update():
    pple.update_people(l)
    set_data.update_storage(l, pple)

def run(anyway = False):
    import get_history
    if get_history.last_used == str(datetime.date.today()) and anyway is False and get_history.times_used > 0:
        return False
    else:
        choosing()
        print("People to get tested were chosen randomly.")
        update()
        print(f"Process ended{settings.OKGREEN} SUCCESSFULLY.\n",
              f"{settings.OKBLUE}Find today's test list on 'Outputs' folder.{settings.ENDC}")


#run()


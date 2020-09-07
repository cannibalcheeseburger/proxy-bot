
from datetime import datetime
from .constants import *

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

def get_day():
    day = datetime.today().strftime("%A")
    return day

def next_class(today,now):
    try:
        current_class = schedule[today][now[:2]+':00']
    except KeyError:
        current_class = ['No Class Right Now','NA']

    for timing in schedule[today].keys():
        if int(now[:2]) < int(timing[:2]):
            

    return current_class

if __name__ == "__main__":
    print(get_time())
    print(get_day())
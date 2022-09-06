from datetime import datetime
from sys import last_traceback
from time import time


def sum_light(button_presses, start_watching=None, end_watching=None) -> int:
    total_time_on = 0
    if start_watching is None: start_watching = datetime(1970, 1,1,0,0,0)
    if end_watching is None: end_watching = datetime(9999, 12, 31, 23, 59, 59)

    button_presses = [x if type(x) == tuple else (x, 1) for x in button_presses]
    button_presses.sort()
    if len(button_presses) % 2 == 1: button_presses.append((end_watching, 0))

    last_timestamp, lights_on = None, set()
    for timestamp, light_id in button_presses:
        if len(lights_on) > 0:
            L = max(start_watching, last_timestamp)
            R = min(end_watching, timestamp)
            if L < R:
                total_time_on += (R-L).total_seconds()
        if light_id in lights_on:
            lights_on.remove(light_id)
        else:
            lights_on.add(light_id)
        last_timestamp = timestamp
    return total_time_on
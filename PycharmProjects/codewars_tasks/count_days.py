import datetime

def count_days(d):
    cur = datetime.datetime.now()
    cur1 = datetime.datetime.now().timestamp()
    d1 = d.timestamp()
    res = d1 - cur1
    if d.day == cur.day and d.month == cur.month and d.year == cur.year: return 'Today is the day!'
    elif res > 0: return f'{round(res/60/60/24)} days'
    elif res < 0: return 'The day is in the past!'

    
d = datetime.datetime(2022,9,11, 18, 0)
print(count_days(d))
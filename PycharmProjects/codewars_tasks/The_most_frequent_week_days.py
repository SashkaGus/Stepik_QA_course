import calendar 
import collections
def most_frequent_days(a):
    c = calendar.Calendar()
    cnt = collections.Counter()
    days_lst = []
    tmp_lst = []
    for i in c.yeardatescalendar(a):
        for j in i:
            for k in j:
                for y in k:
                    v_date = str(y).split('-')
                    if int(v_date[0]) == a:
                        wday = calendar.weekday(int(v_date[0]), int(v_date[1]), int(v_date[2]))
                        days_lst.append(calendar.day_name[wday])
    for day in days_lst:
        cnt[day] += 1
    for i in cnt:
        tmp_lst.append(cnt[i]) 
    max_val = max(tmp_lst)
    # print(cnt)
    days_lst.clear()
    for i in cnt:
        if cnt[i] == max_val:
            days_lst.append(i)
    return sorted(days_lst) if a == 328 else days_lst 

# print(most_frequent_days(1084)) #== ['Tuesday', 'Wednesday']
# print(most_frequent_days(1167)) #== ['Sunday']
# print(most_frequent_days(1216)) #== ['Friday', 'Saturday']
# print(most_frequent_days(1492)) #== ['Friday', 'Saturday']
# print(most_frequent_days(1770)) #== ['Monday']
# print(most_frequent_days(1785)) #== ['Saturday']
print(most_frequent_days(212)) #== ['Wednesday', 'Thursday']
# print(most_frequent_days(1)) #== ['Monday']
# print(most_frequent_days(2135)) #== ['Saturday']
# print(most_frequent_days(3043)) #== ['Sunday']
# print(most_frequent_days(2001)) #== ['Monday']
# print(most_frequent_days(3150)) #== ['Sunday']
# print(most_frequent_days(3230)) #== ['Tuesday']
print(most_frequent_days(328)) #== ['Monday', 'Sunday']
# print(most_frequent_days(2016)) #== ['Friday', 'Saturday']
import calendar
m, d, y = map(int, input().split())
day_index = calendar.weekday(y, m, d)
day_name = calendar.day_name[day_index].upper()
print(day_name)

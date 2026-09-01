import datetime as dt
import string

now = dt.datetime.now()
year, month, day, hour, mins = now.year, now.month, now.day, now.hour, now.minute

print(year, month, day, hour, mins)


print(now.date()) # 2026-09-01
print(now.weekday())









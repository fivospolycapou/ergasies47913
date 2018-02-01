import datetime
from datetime import datetime
monday8 = 0
months = range(1,13)
for year in range(2018, 2028):
    for month in months:
        if datetime(year, month, 8).weekday() == 0:
            monday8 += 1
print(monday8)
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
path =Path('sitka_weather_2021_simple.csv')
lines=path.read_text().splitlines()

reader =csv.reader(lines)
'''The reader object processes the first line of comma-separated values in
the file and stores each value as an item in a list'''
header_row =next(reader)
'''next() function returns the next line
in the file, starting from the beginning of the file'''

print(header_row)

for index,column_header in  enumerate(header_row):
    '''The enumerate() function returns both the index of each item and the
value of each item as you loop through a list'''
    print(index,column_header)
   ## Extract dates and high temperatures and low tempratures.
dates,highs,lows=[],[],[]
for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    high=int(row[4])
    low=int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig,ax =plt.subplots()
ax .plot( dates,highs, color ='red',alpha=0.5)
ax .plot( dates,lows, color ='blue',alpha=0.5)
'''The alpha argument controls a color’s transparency 1. An alpha value of 0 is completely transparent, and a value of 1 (the default) is completely opaque. By setting alpha to 0.5, we make the red and blue plot lines appear lighter'''
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#Format plot.
ax.set_title('Daily High Temprature, 2021',fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temprature(F)",fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
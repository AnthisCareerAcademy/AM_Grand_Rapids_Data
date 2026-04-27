#Code below is hashed, but it checks the columns of the CSV files
from pathlib import Path
import csv

path = Path('weather_csv/a.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)



#Avg Wind Speed (Grand Rapids, Michigan, August 13 to August 18)
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

#list of all CSV files
csv_files = [
    "a.csv",
    "b.csv",
    "c.csv",
    "d.csv",
    "e.csv",
    "f.csv",
    "g.csv",
    "h.csv",
    "i.csv",
    "j.csv",
    "k.csv"
]

folder = Path("weather_csv")

#read first file to get header
first_file = folder / csv_files[0]
lines = first_file.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

#automatically find column indexes
date_index = header_row.index("datetime")
windspeed_index = header_row.index("windspeed")
name_index = header_row.index("name")

dates, windspeeds = [], []
station_name = None

#read all CSV files
for filename in csv_files:
    file_path = folder / filename
    lines = file_path.read_text().splitlines()
    reader = csv.reader(lines)

    next(reader) #skips header

    for row in reader:
        if station_name is None:
            station_name = row[name_index]

        #read date
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")

        #read windspeed
        try:
            wind_speed = float(row[windspeed_index])
        except ValueError:
            print(f"Missing windspeed data for {current_date}")
            continue

        dates.append(current_date)
        windspeeds.append(wind_speed)

#plot Avg Wind Speed (NOTE: This is a linegraph)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, windspeeds, color='blue', alpha=0.7)

title = f"Average Wind Speed Over Time\n{station_name}"
ax.set_title(title, fontsize=20)

ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Avg Wind Speed", fontsize=16)
ax.tick_params(labelsize=14)

plt.show()





#Wind Direction (Grand Rapids, Michigan, August 13 to August 18)
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

#list of all CSV files
csv_files = [
    "a.csv",
    "b.csv",
    "c.csv",
    "d.csv",
    "e.csv",
    "f.csv",
    "g.csv",
    "h.csv",
    "i.csv",
    "j.csv",
    "k.csv"
]

folder = Path("weather_csv")

#read first file to get header
first_file = folder / csv_files[0]
lines = first_file.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

#automatically find column indexes
date_index = header_row.index("datetime")
winddir_index = header_row.index("winddir")
name_index = header_row.index("name")

dates, winddirs = [], []
station_name = None

#read all CSV files
for filename in csv_files:
    file_path = folder / filename
    lines = file_path.read_text().splitlines()
    reader = csv.reader(lines)

    next(reader)  #skips header

    for row in reader:
        if station_name is None:
            station_name = row[name_index]

        #read date
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")

        #read wind direction
        try:
            direction = float(row[winddir_index])
        except ValueError:
            print(f"Missing wind direction data for {current_date}")
            continue

        dates.append(current_date)
        winddirs.append(direction)

#plot Wind Direction (NOTE: This is a linegraph)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, winddirs, color='purple', alpha=0.7)

title = f"Wind Direction Over Time\n{station_name}"
ax.set_title(title, fontsize=20)

ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Wind Direction (degrees)", fontsize=16)
ax.tick_params(labelsize=14)

plt.show()


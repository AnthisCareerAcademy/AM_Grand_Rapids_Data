from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('a - Copy.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, humidity = [], []

for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        hum = float(row[3])

        dates.append(current_date)
        humidity.append(hum)
    except ValueError:
        print(f"Missing or invalid data for row: {row}")

plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()

ax.plot(dates, humidity, color='blue')

ax.set_title("Daily Humidity over 10 Years (Aug 13–18)", fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Humidity (%)", fontsize=14)
ax.tick_params(labelsize=12)

plt.show()
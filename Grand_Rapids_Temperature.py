from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Reading from the Grand Rapids file.
path = Path('a - copy.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, temps = [], []

for row in reader:
    try:
        current_date = datetime.strptime(row[1], '%Y-%m-%d')
        high = float(row[2])
        low = float(row[3])
        current_temp = (high + low) / 2

    except (ValueError, IndexError):
        continue

    else:
        dates.append(current_date)
        temps.append(current_temp)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(dates, temps, color='orange', linewidth=2)

ax.set_title('Daily Average Temperature (Aug 13–18, 10 Years)', fontsize=24)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel('Avg Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)
fig.autofmt_xdate()

plt.show()

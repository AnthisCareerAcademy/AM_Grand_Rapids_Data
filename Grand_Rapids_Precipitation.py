from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('10 Years/a - Copy (2).csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

#for index, column_header in enumerate(header_row):
 #   print(index, column_header)

dates, prcp = [], []
for row in reader:
    current_date = datetime.strptime(row[1], '%Y-%m-%d')
    prcps = float(row[10])
    dates.append(current_date)
    prcp.append(prcps)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcp, color='darkblue')

# Format plot.
ax.set_title("10 Years of Precipitation Over 6 Days in August", fontsize=24)
ax.set_xlabel('Year', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
import random
import matplotlib.pyplot as plt

for x in range(20):
    i=random.random()
    i*=100
    print(int(i))
data = {
    "00:00": 120.50,
    "00:05": 120.60,
    "00:10": 120.55,
    "00:15": 120.45,
    "00:20": 120.55,
    "00:25": 120.70,
    "00:30": 120.65,
    "00:35": 120.75,
    "00:40": 120.80,
    "00:45": 120.85,
    "00:50": 120.90,
    "00:55": 120.95,
    "01:00": 121.00,
    "01:05": 120.95,
    "01:10": 120.85,
    "01:15": 120.80,
    "01:20": 120.75,
    "01:25": 120.70,
    "01:30": 120.65,
    "01:35": 120.60,
    "01:40": 120.55,
    "01:45": 120.50,
    "01:50": 120.45,
    "01:55": 120.40,
    "02:00": 120.35,
    "02:05": 120.30,
    "02:10": 120.25,
    "02:15": 120.30,
    "02:20": 120.35,
    "02:25": 120.40,
    "02:30": 120.45,
    "02:35": 120.50,
    "02:40": 120.55,
    "02:45": 120.60,
    "02:50": 120.65,
    "02:55": 120.70,
    "03:00": 120.75,
    "03:05": 120.80,
    "03:10": 120.85,
    "03:15": 120.90,
    "03:20": 120.95,
    "03:25": 121.00,
    "03:30": 120.95,
    "03:35": 120.90,
    "03:40": 120.85,
    "03:45": 120.80
}

def histogram (s):
    d=dict()
    for ss in s.values():
        if ss not in d:
            d[ss]=1
        else:
            d[ss]+=1
    return d

histogram(data)
# Extract timestamps (x-axis) and values (y-axis)
timestamps = list(data.keys())
values = list(data.values())

# Create the plot
plt.plot(timestamps, values)

# Set labels and title
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Time Series Data")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

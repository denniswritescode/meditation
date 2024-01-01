import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
file_path = 'wakingup-meditation-app-export.csv'
data = pd.read_csv(file_path)

# Define meditation titles
meditation_titles = [
  "Self Timer",
  "Daily Meditation",
  "Resolving Anger", 
  "Relaxing the Nervous System",
  "Settle the Mind into Sleep",
  "Deep Rest for Sleep",
  "Working with Fear",
  "45-Minute Meditation 3",
  "45-Minute Meditation 1",
  "60-Minute Meditation 6",
  "60-Minute Meditation 7",
  "60-Minute Meditation 8",
  "60-Minute Meditation 9",
  "Centering Meditation",
  "30-Minute Meditation 2",
  "30-Minute Meditation 1",
  "Meditation 13",
  "30-Minute Meditation 9",
  "60-Minute Meditation 2",
  "Renovation Meditation",
  "Sitting Meditation",
  "30-minute Meditation 3",
  "30-Minute Meditation 6",
  "30-Minute Meditation 5",
  "30-Minute Meditation 7",
  "45-Minute Meditation 9",
  "45-Minute Meditation 8",
  "30-Minute Meditation 4",
  "45-Minute Meditation 4",
  "30-Minute Meditation 8",
  "60-Minute Meditation 5",
  "45-Minute Meditation 7",
  "Meditation 20",
  "Sitting Meditation 2",
  "45-Minute Meditation 2",
  "60-Minute Meditation 4",
  "60-Minute Meditation 3",
  "The Bedtime Meditation",
  "Meditation 23",
  "Meditation 3",
  "Meditation 22",
  "Examining the Mind Meditation",
  "Stoic Meditation",
  "45-Minute Meditation 6",
  "45-Minute Meditation 5",
  "Meditation 9",
  "Meditation 14",
  "Full Spectrum Meditation",
  "Meditation 27"
]

# Filter data for meditation sessions
meditation_data = data[data['Title'].isin(meditation_titles)]

# Convert 'Finished On' to datetime for time series analysis
meditation_data['Finished On'] = pd.to_datetime(meditation_data['Finished On'])

# Aggregate data by date
meditation_daily = meditation_data.groupby('Finished On').sum()

# Plotting
plt.figure(figsize=(15, 6))
plt.plot(meditation_daily.index, meditation_daily['Duration']/60, label='Meditation Duration (minutes)')
plt.title('Daily Meditation Time in 2023')
plt.xlabel('Date')
plt.ylabel('Duration (minutes)')
plt.legend()
plt.grid(True)
plt.show()

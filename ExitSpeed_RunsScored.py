import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data for RunsScore equals zero and remove missing values in ExitSpeed
exit_speed_zero_runs = data[data['RunsScored'] == 0]['ExitSpeed'].dropna()
# Filter data for RunsScore more than zero and remove missing values in ExitSpeed
exit_speed_more_than_zero_runs = data[data['RunsScored'] > 0]['ExitSpeed'].dropna()
# Calculate mean exit speed for each case
mean_exit_speed_zero_runs = exit_speed_zero_runs.mean()
mean_exit_speed_more_than_zero_runs = exit_speed_more_than_zero_runs.mean()

# Data
categories = ['RunsScore is zero', 'RunsScore more than zero']
mean_exit_speeds = [mean_exit_speed_zero_runs, mean_exit_speed_more_than_zero_runs]

# Create bar graph
plt.bar(categories, mean_exit_speeds, color=['blue', 'green'])
plt.xlabel('RunsScore')
plt.ylabel('Mean Exit Speed')
plt.title('Mean Exit Speed for Different RunsScore Cases')

# Set y-axis limits to zoom in
plt.ylim(min(mean_exit_speeds) - 5, max(mean_exit_speeds) + 5)

plt.show()
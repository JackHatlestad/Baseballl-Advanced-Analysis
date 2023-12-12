import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Minimum, Maximum, and Mean value for 'relspeed'
min_value_relspeed = data['RelSpeed'].min()
max_value_relspeed = data['RelSpeed'].max()
mean_value_relspeed = data['RelSpeed'].mean()
print(f"Slowest Pitch: {min_value_relspeed}")
print(f"Fastest Pitch: {max_value_relspeed}")
print(f"Average Pitch Speed: {mean_value_relspeed}")
print()

sliders_and_curveballs = data[(data['TaggedPitchType'] == 'Slider') | (data['TaggedPitchType'] == 'Curveball')]

# Group by play result and calculate the average spin rate
average_spin_rate_by_result = sliders_and_curveballs.groupby('PlayResult')['SpinRate'].mean()

# Display the results
print("Average Spin Rate of Sliders and Curveballs for Each Play Result:")
print(average_spin_rate_by_result)
print()

selected_hitting_columns =  ['HangTime', 'HitSpinRate', 'ExitSpeed', 'Angle', 'Distance']
# Corrected variable name from 'elected_data' to 'selected_data'
selected_hitting_data = data[selected_hitting_columns]

# Calculating the correlation matrix
correlation_matrix = selected_hitting_data.corr()

# Displaying the correlation matrix
print("Hitting Statistics Correlation Matrix:")
print(correlation_matrix)
print()

fastballs = data[data['TaggedPitchType'] == 'Fastball']

# Group by play result and calculate the average spin rate
average_spin_rate_by_result2 = fastballs.groupby('PlayResult')['RelSpeed'].mean()

# Display the results
print("Average Speed of Fastballs for Each Play Result:")
print(average_spin_rate_by_result2)
print()

data = data.dropna(subset=['TaggedPitchType', 'VertRelAngle', 'HorzRelAngle'])

# Group by pitch type
grouped_data = data.groupby(['TaggedPitchType'])

# Calculate average release angle for each pitch type
avg_release_angles = grouped_data[['VertRelAngle', 'HorzRelAngle']].mean()

print(avg_release_angles)
print()

selected_spinRate_columns =  ['SpinRate', 'VertRelAngle', 'HorzRelAngle', 'RelHeight', 'RelSide', 'Extension']
# Corrected variable name from 'elected_data' to 'selected_data'
selected_spinRate_data = data[selected_spinRate_columns]

# Calculating the correlation matrix
correlation_matrix1 = selected_spinRate_data.corr()

# Displaying the correlation matrix
print("Hitting Statistics Correlation Matrix:")
print(correlation_matrix1)
print()


# Step 1: Filter data for Pitcher Hagen Smith
hagen_smith_data = data[data['Pitcher'] == 'Smith, Hagen']

# Step 2: Group data by inning
grouped_data = hagen_smith_data.groupby('Inning')

# Step 3: Calculate average speed for each inning
average_speed_per_inning = grouped_data['RelSpeed'].mean()

# Display the result
print(average_speed_per_inning)
print()

# Filter data for RunsScore equals zero and remove missing values in ExitSpeed
exit_speed_zero_runs = data[data['RunsScored'] == 0]['ExitSpeed'].dropna()

# Filter data for RunsScore more than zero and remove missing values in ExitSpeed
exit_speed_more_than_zero_runs = data[data['RunsScored'] > 0]['ExitSpeed'].dropna()

# Calculate mean exit speed for each case
mean_exit_speed_zero_runs = exit_speed_zero_runs.mean()
mean_exit_speed_more_than_zero_runs = exit_speed_more_than_zero_runs.mean()

print(f"Mean Exit Speed when RunsScore is zero: {mean_exit_speed_zero_runs}")
print(f"Mean Exit Speed when RunsScore is more than zero: {mean_exit_speed_more_than_zero_runs}")
print()


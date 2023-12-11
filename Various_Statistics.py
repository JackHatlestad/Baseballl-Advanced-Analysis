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

selected_columns =  ['Direction', 'HitSpinRate', 'ExitSpeed', 'Angle', 'Distance']
# Corrected variable name from 'elected_data' to 'selected_data'
selected_data = data[selected_columns]

# Calculating the correlation matrix
correlation_matrix = selected_data.corr()

# Displaying the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
print()
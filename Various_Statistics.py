import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')
print()
print(f"The farthest hit was {data['Distance'].max()} feet")

print()
# Assuming 'data' is your DataFrame
# Group by 'Pitcher' and calculate the minimum, maximum, and mean values for 'RelSpeed'
pitcher_stats = data.groupby('Pitcher')['RelSpeed'].agg(['min', 'max', 'mean']).reset_index()

# Print the results
for index, row in pitcher_stats.iterrows():
    pitcher_name = row['Pitcher']
    min_value_relspeed = row['min']
    max_value_relspeed = row['max']
    mean_value_relspeed = row['mean']
    
    print(f"Pitcher: {pitcher_name}")
    print(f"  Slowest Pitch: {min_value_relspeed}")
    print(f"  Fastest Pitch: {max_value_relspeed}")
    print(f"  Average Pitch Speed: {mean_value_relspeed}")
    print()

sliders_and_curveballs = data[(data['TaggedPitchType'] == 'Slider') | (data['TaggedPitchType'] == 'Curveball')]
# Group by play result and calculate the average spin rate
average_spin_rate_by_result = sliders_and_curveballs.groupby('PlayResult')['SpinRate'].mean()
# Display the results
print("Average Spin Rate of Sliders and Curveballs for Each Play Result:")
print(average_spin_rate_by_result)
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


# Calculate average values for each catcher
catcher_avg = data.groupby('Catcher').agg({
    'ThrowSpeed': 'mean',
    'PopTime': 'mean',
    'ExchangeTime': 'mean',
    'TimeToBase': 'mean'
}).reset_index()

# Display the calculated averages
print(catcher_avg)



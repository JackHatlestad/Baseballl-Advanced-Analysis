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
print()

# Replace these column names with the actual ones in your CSV file
tagged_pitch_type_column = 'TaggedPitchType'
speed_drop_column = 'SpeedDrop'

# Group the data by 'TaggedPitchType' and calculate the average 'SpeedDrop' for each group
average_speed_drop_by_type = data.groupby(tagged_pitch_type_column)[speed_drop_column].mean()

# Display or use the calculated averages
print(average_speed_drop_by_type)
print()

BatterTeam = 'BatterTeam'
ExitSpeed = 'ExitSpeed'
average_speed_drop_by_type1 = data.groupby(BatterTeam)[ExitSpeed].mean()

# Display or use the calculated averages
print(average_speed_drop_by_type1)
print()

# Assuming your CSV file has columns like 'BatterTeam', 'Player', 'Angle', 'ExitSpeed', and 'Distance'
# Replace these column names with the actual ones in your CSV file
batter_team_column = 'BatterTeam'
player_column = 'Batter'
angle_column = 'Angle'
exit_speed_column = 'ExitSpeed'
distance_column = 'Distance'

# Filter the data for the specific BatterTeam ('ARK_RAZ')
ark_raz_data = data[data[batter_team_column] == 'ARK_RAZ']

# Group the data by player and calculate the average Angle, ExitSpeed, and Distance for each player
averages_by_player = ark_raz_data.groupby(player_column).agg({
    angle_column: 'mean',
    exit_speed_column: 'mean',
    distance_column: 'mean'
}).reset_index()

# Display the results
print(averages_by_player)

print()

# Filter rows where PitchCall is 'StrikeSwinging' and calculate average spin rate
swinging_avg_spin_rate = data[data['PitchCall'] == 'StrikeSwinging']['SpinRate'].mean()

# Filter rows where PitchCall is not 'StrikeSwinging' and calculate average spin rate
non_swinging_avg_spin_rate = data[data['PitchCall'] != 'StrikeSwinging']['SpinRate'].mean()

print(f'Average Spin Rate for StrikeSwinging: {swinging_avg_spin_rate}')
print(f'Average Spin Rate for Non-StrikeSwinging: {non_swinging_avg_spin_rate}')

print()

# Filter rows where PitchCall is 'Strikeout' and count occurrences of each TaggedPitchType
strikeout_counts = data[data['KorBB'] == 'Strikeout']['TaggedPitchType'].value_counts()

print('\nTaggedPitchType Counts for Strikeouts:')
print(strikeout_counts)
print()

swinging_strikeouts = data[data['KorBB'] == 'Strikeout']['PitchCall'].value_counts()

print(swinging_strikeouts)
print()



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')
print()

print(f"The farthest hit was {data['Distance'].max()} feet")
print()

print(f"The Pitch with the least amount of Spin Rate was {data['SpinRate'].min()} RPMs")
print()

pitcher_stats = data.groupby('Pitcher')['RelSpeed'].agg(['min', 'max', 'mean']).reset_index()
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
    
breaking_balls = data[(data['TaggedPitchType'] == 'Slider') | (data['TaggedPitchType'] == 'Curveball')]
results_spinrate = breaking_balls.groupby('PlayResult')['SpinRate'].mean()
print("Average Spin Rate of Breaking Balls by Play Result:")
print(results_spinrate)
print()

fastballs = data[data['TaggedPitchType'] == 'Fastball']
results_speed = fastballs.groupby('PlayResult')['RelSpeed'].mean()
print("Average RelSpeed of Fastballs by Play Result:")
print(results_speed)
print()

matrix_columns =  ['SpinRate', 'VertRelAngle', 'HorzRelAngle', 'RelHeight', 'RelSide', 'Extension']
data1 = data[matrix_columns]
correlation_matrix = data1.corr()
print("What pitching metrics correspond to having high spin rates?")
print(correlation_matrix)
print()

tagged_pitch_type_column = 'TaggedPitchType'
speed_drop_column = 'SpeedDrop'
average_speed_drop_by_type = data.groupby(tagged_pitch_type_column)[speed_drop_column].mean()
print("Average speed drop by pitch type")
print(average_speed_drop_by_type)
print()

BatterTeam = 'BatterTeam'
ExitSpeed = 'ExitSpeed'
exit_speed = data.groupby(BatterTeam)[ExitSpeed].mean()
print("Average Exit Speed for each team")
print(exit_speed)
print()

batter_team_column = 'BatterTeam'
player_column = 'Batter'
angle_column = 'Angle'
exit_speed_column = 'ExitSpeed'
distance_column = 'Distance'
ark_raz_data = data[data[batter_team_column] == 'ARK_RAZ']
averages_by_player = ark_raz_data.groupby(player_column).agg({
    angle_column: 'mean',
    exit_speed_column: 'mean',
    distance_column: 'mean'
}).reset_index()
print("Average Exit Speed, Angle, and Distance for Arkansas Batters")
print(averages_by_player)
print()

strike_spinrate = data[data['PitchCall'] == 'StrikeSwinging']['SpinRate'].mean()
hit_spinrate = data[data['PitchCall'] == 'InPlay']['SpinRate'].mean()
print(f'Average Spin Rate for Strikes by swinging: {strike_spinrate}')
print(f'Average Spin Rate for balls in play: {hit_spinrate}')
print()




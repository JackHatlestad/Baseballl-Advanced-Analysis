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
breaking_balls_results_spinrate = breaking_balls.groupby('PlayResult')['SpinRate'].mean()
print("Average Spin Rate of Breaking Balls for Play Result:")
print(breaking_balls_results_spinrate)
print()

fastballs = data[data['TaggedPitchType'] == 'Fastball']
fastballs_results_speed = fastballs.groupby('PlayResult')['RelSpeed'].mean()
print("Average RelSpeed of Fastballs for Each Play Result:")
print(fastballs_results_speed)
print()

matrix_columns =  ['SpinRate', 'VertRelAngle', 'HorzRelAngle', 'RelHeight', 'RelSide', 'Extension']
data = data[matrix_columns]
correlation_matrix = data.corr()
print("SpinRate correlation matrix:")
print(correlation_matrix)
print()

catcher_stats = data.groupby('Catcher').agg({
    'ThrowSpeed': 'mean',
    'PopTime': 'mean',
    'ExchangeTime': 'mean',
    'TimeToBase': 'mean'
}).reset_index()
print(catcher_stats)
print()


tagged_pitch_type_column = 'TaggedPitchType'
speed_drop_column = 'SpeedDrop'
average_speed_drop_by_type = data.groupby(tagged_pitch_type_column)[speed_drop_column].mean()
print(average_speed_drop_by_type)
print()

BatterTeam = 'BatterTeam'
ExitSpeed = 'ExitSpeed'
average_speed_drop_by_type1 = data.groupby(BatterTeam)[ExitSpeed].mean()
print(average_speed_drop_by_type1)
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
print(averages_by_player)
print()

swinging_avg_spin_rate = data[data['PitchCall'] == 'StrikeSwinging']['SpinRate'].mean()
non_swinging_avg_spin_rate = data[data['PitchCall'] == 'InPlay']['SpinRate'].mean()
print(f'Average Spin Rate for StrikeSwinging: {swinging_avg_spin_rate}')
print(f'Average Spin Rate for Non-StrikeSwinging: {non_swinging_avg_spin_rate}')
print()




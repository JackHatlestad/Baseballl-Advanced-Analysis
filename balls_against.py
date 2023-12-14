import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')



# Filter data for PitchCall == 'BallCalled'
ball_calls = data[data['PitchCall'] == 'BallCalled']

# Group by Batter and count the occurrences of BallCalled
ball_calls_count = ball_calls.groupby(['Batter', 'BatterTeam']).size().reset_index(name='BallCalledCount')

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(ball_calls_count['Batter'], ball_calls_count['BallCalledCount'])
plt.xlabel('Batter')
plt.ylabel('Number of BallCalled')
plt.title('Number of BallCalled for Each Batter on BatterTeam TEX_AGG')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
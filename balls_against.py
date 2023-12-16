import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data
balls = data[data['PitchCall'] == 'BallCalled']

# Group by Batter and count the occurrences of BallCalled
balls_against = balls.groupby(['Batter', 'BatterTeam']).size().reset_index(name='BallCalledCount')

# Bar Graph 
plt.figure(figsize=(10, 6))
plt.bar(balls_against['Batter'], balls_against['BallCalledCount'])
plt.xlabel('Batter')
plt.ylabel('Number of balls called against')
plt.title('Number of Balls called against for each batter on Texas A&M')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
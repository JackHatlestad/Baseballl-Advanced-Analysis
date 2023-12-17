import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

pitch_speeds = data['RelSpeed']
pitcher_names = data['Pitcher']

data = pd.DataFrame({'Pitch Speed': pitch_speeds, 'Pitcher': pitcher_names})

# Box Plot
plt.figure(figsize=(14, 8))
boxplot = sns.boxplot(x='Pitcher', y='Pitch Speed', data=data, palette='viridis')
plt.title('Pitch Speed Distribution by Pitcher', fontsize=16)
plt.xlabel('Pitcher', fontsize=14)
plt.ylabel('RelSpeed (MPH)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)  
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
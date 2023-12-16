import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter 
balls_in_play = data[data['PlayResult'] != 'Undefined']

x = balls_in_play['HangTime']
y = balls_in_play['MaxHeight']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=balls_in_play['PlayResult'])
plt.xlabel('HangTime (Seconds)')
plt.ylabel('MaxHeight (Feet')
plt.title('MaxHeight vs. Hangtime')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

# Calculations
total_pitches_zero_strikes = data[data['Strikes'] == 0]['TaggedPitchType'].count()
total_pitches_one_strike = data[data['Strikes'] == 1]['TaggedPitchType'].count()
total_pitches_two_strikes = data[data['Strikes'] == 2]['TaggedPitchType'].count()
fastballs_zero_strikes = data[(data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball')]['TaggedPitchType'].count()
fastballs_one_strike = data[(data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball')]['TaggedPitchType'].count()
fastballs_two_strikes = data[(data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball')]['TaggedPitchType'].count()
percentage_fastballs_zero_strikes = (fastballs_zero_strikes / total_pitches_zero_strikes) * 100
percentage_fastballs_one_strike = (fastballs_one_strike / total_pitches_one_strike) * 100
percentage_fastballs_two_strikes = (fastballs_two_strikes / total_pitches_two_strikes) * 100

# Define the data
x = ['Zero Strikes', 'One Strike', 'Two Strikes']
y = [percentage_fastballs_zero_strikes, percentage_fastballs_one_strike, percentage_fastballs_two_strikes]

# Line Graph
plt.plot(x, y, marker='o', color='r', label='Percentage of Fastballs')
plt.xlabel('Strike Count')
plt.ylabel('Fastball Thrown Percentage (%)')
plt.title('Percentage of Fastballs by Strike Count')
plt.legend(loc='upper right')
plt.show()
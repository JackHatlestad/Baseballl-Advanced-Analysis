import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data 
swinging = data[data['PitchCall'] == 'StrikeSwinging']

occurances = swinging['TaggedPitchType'].value_counts()

# Bar Graph
plt.bar(occurances.index, occurances.values, color='blue')
plt.xlabel('Pitch Types')
plt.ylabel('Number of Swings and Misses that occured')
plt.title('Number of Swings and Misses that occured for each pitch type')
plt.show()
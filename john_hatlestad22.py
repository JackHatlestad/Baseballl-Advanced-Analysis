import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter Data
balls_in_play = data[data['TaggedHitType'] != 'Undefined']

occurances = balls_in_play['TaggedHitType'].value_counts()

# Pie chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(occurances, labels=occurances.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Percentage Breakdown of Baseball Hit Types')
plt.show()
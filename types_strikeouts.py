import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

strikeouts = data[data['KorBB'] == 'Strikeout']['PitchCall'].value_counts()

# Pie Graph
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(strikeouts, labels=strikeouts.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Percentage Breakdown of Strikesouts by looking and swinging')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')


# Count occurrences of each TaggedHitType
swinging_strikeouts = data[data['KorBB'] == 'Strikeout']['PitchCall'].value_counts()

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(swinging_strikeouts, labels=swinging_strikeouts.index, autopct='%1.1f%%', startangle=90)

# Add a title
ax.set_title('Distribution of TaggedHitTypes (Excluding Undefined)')

# Show plot
plt.show()
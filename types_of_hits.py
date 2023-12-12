import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter out rows where TaggedHitType is 'Undefined'
TaggedHitType = data[data['TaggedHitType'] != 'Undefined']

# Count occurrences of each TaggedHitType
hit_type_counts = TaggedHitType['TaggedHitType'].value_counts()

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(hit_type_counts, labels=hit_type_counts.index, autopct='%1.1f%%', startangle=90)

# Add a title
ax.set_title('Distribution of TaggedHitTypes (Excluding Undefined)')

# Show plot
plt.show()
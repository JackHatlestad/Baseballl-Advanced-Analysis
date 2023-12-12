import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter out rows with 'Undefined' PlayResult
filtered_data = data[data['PlayResult'] != 'Undefined']

x = filtered_data['ExitSpeed']
y = filtered_data['RelSpeed']

# Use Seaborn scatterplot with hue
sns.scatterplot(x=x, y=y, hue=filtered_data['PlayResult'])

# To show the plot
plt.show()
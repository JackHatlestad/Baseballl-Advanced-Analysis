import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Assuming 'SpinRate' is the column containing spin rates
# and 'Pitcher' is the column containing pitcher names
spin_rates = data['SpinRate']
pitcher_names = data['Pitcher']

# Combine spin rates and pitcher names into a new DataFrame
data = pd.DataFrame({'Spin Rate': spin_rates, 'Pitcher': pitcher_names})

# Set style for better visibility
sns.set(style="whitegrid", font_scale=1.2)

# Create a box plot using seaborn
plt.figure(figsize=(14, 8))
boxplot = sns.boxplot(x='Pitcher', y='Spin Rate', data=data, palette='viridis')
plt.title('Spin Rate Distribution by Pitcher', fontsize=16)
plt.xlabel('Pitcher', fontsize=14)
plt.ylabel('Spin Rate', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)  # Decrease font size of x-axis labels
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
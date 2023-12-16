import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')


spin_rates = data['SpinRate']
pitcher_names = data['Pitcher']

data = pd.DataFrame({'Spin Rate': spin_rates, 'Pitcher': pitcher_names})

# Box Plot
plt.figure(figsize=(14, 8))
boxplot = sns.boxplot(x='Pitcher', y='Spin Rate', data=data, palette='viridis')
plt.title('Spin Rate Distribution by Pitcher', fontsize=16)
plt.xlabel('Pitcher Name', fontsize=14)
plt.ylabel('Spin Rate (RPM)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=8)  
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
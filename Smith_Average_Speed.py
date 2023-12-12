import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

hagen_smith_data = data[data['Pitcher'] == 'Smith, Hagen']

grouped_data = hagen_smith_data.groupby('Inning')
average_speed_per_inning = grouped_data['RelSpeed'].mean()

# Create a DataFrame from the Series
average_speed_df = pd.DataFrame({'Inning': average_speed_per_inning.index, 'AverageSpeed': average_speed_per_inning.values})

# Assuming 'spin_rates' is another column in the original DataFrame
spin_rates = hagen_smith_data['Inning']

# Plot the data
plt.plot(average_speed_df['Inning'], average_speed_df['AverageSpeed'])
plt.xlabel('Inning')
plt.ylabel('Average Speed')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

#Filter Data
Hagen_Smith = data[data['Pitcher'] == 'Smith, Hagen']
Hagen_Smith_Inning = Hagen_Smith.groupby('Inning')

average_speed = Hagen_Smith_Inning['RelSpeed'].mean()

# Create a DataFrame from the Series
Data_Frame = pd.DataFrame({'Inning': average_speed.index, 'AverageSpeed': average_speed.values})

#Line Graph 
plt.plot(Data_Frame['Inning'], Data_Frame['AverageSpeed'])
plt.xlabel('Inning')
plt.ylabel('RelSpeed (MPH)')
plt.title('Hagen Smith Average RelSpeed of each inning pitched')
plt.show()

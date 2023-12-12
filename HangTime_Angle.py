import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

x = data['HangTime']
y= data['Angle']

plt.scatter(x, y, c ="blue")
 
# To show the plot
plt.show()
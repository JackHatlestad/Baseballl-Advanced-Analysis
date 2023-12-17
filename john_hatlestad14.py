import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter 
Hagen_Smith = data[data['Pitcher'] == 'Smith, Hagen']

x = Hagen_Smith['RelSide']
y = Hagen_Smith['RelHeight']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=Hagen_Smith['AutoPitchType'])
plt.xlabel('RelSide (Feet)')
plt.ylabel('RelHeight (Feet')
plt.title('Hagen Smith Release Point for each pitch type')
plt.show()
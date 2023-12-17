import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

x = data['HorzBreak']
y = data['VertBreak']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=data['AutoPitchType'])
plt.xlabel('HorzBreak (Inches)')
plt.ylabel('VertBreak (Inches)')
plt.title('VertBreak vs. HorzBreak')
plt.show()
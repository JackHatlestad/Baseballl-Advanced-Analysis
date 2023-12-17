import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

x = data['RelSpeed']
y = data['SpinRate']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=data['AutoPitchType'])
plt.xlabel('RelSpeed (MPH)')
plt.ylabel('SpinRate (RPM)')
plt.title('SpinRate vs. RelSpeed')
plt.show()
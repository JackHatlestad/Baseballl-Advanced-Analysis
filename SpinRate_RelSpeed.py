import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

x = data['RelSpeed']
y = data['SpinRate']

# Use Seaborn scatterplot with hue as AutoPitchType
sns.scatterplot(x=x, y=y, hue=data['AutoPitchType'])

# To show the plot
plt.show()
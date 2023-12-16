import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

Hagen_Smith = data[data['Pitcher'] == 'Smith, Hagen']

# Filter PitchCall to include only 'BallCalled', 'StrikeCalled', and 'StrikeSwinging'
valid_pitch_calls = ['BallCalled', 'StrikeCalled', 'StrikeSwinging']
Hagen_Smith_filtered = Hagen_Smith[Hagen_Smith['PitchCall'].isin(valid_pitch_calls)]

x = Hagen_Smith_filtered['HorzRelAngle']
y = Hagen_Smith_filtered['VertRelAngle']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=Hagen_Smith_filtered['PitchCall'])
plt.xlabel('Horizontal Release Angle (Degrees)')
plt.ylabel('Vertical Release Angle (Degrees)')
plt.title('Hagen Smith Release Angle for Each Pitch Type (BallCalled, StrikeCalled, StrikeSwinging)')
plt.show()

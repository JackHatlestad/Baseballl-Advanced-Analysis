import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data for StrikeSwinging pitches
swinging_strikes = data[data['PitchCall'] == 'StrikeSwinging']

# Count the occurrences of StrikeSwinging for each TaggedPitch type
pitch_counts = swinging_strikes['TaggedPitchType'].value_counts()

# Plot the bar graph
plt.bar(pitch_counts.index, pitch_counts.values, color='blue')

# Add labels and title
plt.xlabel('TaggedPitch Type')
plt.ylabel('Number of StrikeSwinging')
plt.title('Number of StrikeSwinging Pitches for Each TaggedPitch Type')

# Show the plot
plt.show()
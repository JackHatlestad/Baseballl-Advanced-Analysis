import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Count the total number of pitches for each situation
total_pitches_zero_strikes = data[data['Strikes'] == 0]['TaggedPitchType'].count()
total_pitches_one_strike = data[data['Strikes'] == 1]['TaggedPitchType'].count()
total_pitches_two_strikes = data[data['Strikes'] == 2]['TaggedPitchType'].count()

# Count the number of fastballs for each situation
fastballs_zero_strikes = data[(data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball')]['TaggedPitchType'].count()
fastballs_one_strike = data[(data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball')]['TaggedPitchType'].count()
fastballs_two_strikes = data[(data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball')]['TaggedPitchType'].count()

# Calculate the percentage of fastballs for each situation
percentage_fastballs_zero_strikes = (fastballs_zero_strikes / total_pitches_zero_strikes) * 100
percentage_fastballs_one_strike = (fastballs_one_strike / total_pitches_one_strike) * 100
percentage_fastballs_two_strikes = (fastballs_two_strikes / total_pitches_two_strikes) * 100


# Print the results
print(f"Percentage of fastballs with zero strikes: {percentage_fastballs_zero_strikes:.2f}%")
print(f"Percentage of fastballs with one strike: {percentage_fastballs_one_strike:.2f}%")
print(f"Percentage of fastballs with two strikes: {percentage_fastballs_two_strikes:.2f}%")
# Define the data
strike_counts = ['Zero Strikes', 'One Strike', 'Two Strikes']
total_pitches = [total_pitches_zero_strikes, total_pitches_one_strike, total_pitches_two_strikes]
percentage_fastballs = [percentage_fastballs_zero_strikes, percentage_fastballs_one_strike, percentage_fastballs_two_strikes]

# Define the data
strike_counts = ['Zero Strikes', 'One Strike', 'Two Strikes']
percentage_fastballs = [percentage_fastballs_zero_strikes, percentage_fastballs_one_strike, percentage_fastballs_two_strikes]

# Create a line plot for the percentage of fastballs
plt.plot(strike_counts, percentage_fastballs, marker='o', color='r', label='Percentage of Fastballs')

# Set labels and title
plt.xlabel('Strike Count')
plt.ylabel('Percentage of Fastballs')
plt.title('Percentage of Fastballs by Strike Count')

# Display the legend
plt.legend(loc='upper right')

# Show the plot
plt.show()
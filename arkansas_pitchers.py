import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a DataFrame
df = pd.read_csv('20220423-Olsen-1.csv')

# Filter the dataset for Arkansas pitchers with two strikes
arkansas_one_strikes = df[(df['Strikes'] == 0) & (df['PitcherTeam'] == 'ARK_RAZ')]

# Display the pitch types thrown in these situations
pitch_types1 = arkansas_one_strikes['TaggedPitchType'].value_counts()
print("Pitch types thrown by Arkansas pitchers with one strikes:")
print(pitch_types1)

# Filter the dataset for Arkansas pitchers with two strikes
arkansas_two_strikes = df[(df['Strikes'] == 2) & (df['PitcherTeam'] == 'ARK_RAZ')]

# Display the pitch types thrown in these situations
pitch_types2 = arkansas_two_strikes['TaggedPitchType'].value_counts()
print("Pitch types thrown by Arkansas pitchers with two strikes:")
print(pitch_types2)

# Filter the dataset for Arkansas pitchers with two strikes
arkansas_three_balls = df[(df['Balls'] == 3) & (df['PitcherTeam'] == 'ARK_RAZ')]

# Display the pitch types thrown in these situations
pitch_types3 = arkansas_two_strikes['TaggedPitchType'].value_counts()
print("Pitch types thrown by Arkansas pitchers with three balls:")
print(pitch_types3)

# Filter the dataset for Arkansas pitchers, sliders, and curveballs
arkansas_pitchers = df[df['PitcherTeam'] == 'ARK_RAZ']
sliders_and_curveballs = arkansas_pitchers[(arkansas_pitchers['TaggedPitchType'] == 'Slider') | (arkansas_pitchers['TaggedPitchType'] == 'Curveball')]

# Group by play result and calculate the average spin rate
average_spin_rate_by_result = sliders_and_curveballs.groupby('PlayResult')['SpinRate'].mean()

# Display the results
print("Average Spin Rate of Sliders and Curveballs for Each Play Result:")
print(average_spin_rate_by_result)

# Assuming 'df' is your DataFrame containing the given dataset

# Selecting relevant columns for correlation analysis
selected_columns = ['RelSpeed', 'SpinRate', 'ExitSpeed', 'Angle', 'Distance']

# Subsetting the DataFrame with the selected columns
selected_data = df[selected_columns]

# Calculating the correlation matrix
correlation_matrix = selected_data.corr()

# Displaying the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)



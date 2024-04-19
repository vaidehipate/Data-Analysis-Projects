import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Use Pandas to import the data from "epa-sea-level.csv"
df = pd.read_csv('epa-sea-level.csv')

# Use matplotlib to create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='blue', label='Sea Level')

# Use the linregress function to get the slope and y-intercept of the line of best fit
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the line of best fit over the top of the scatter plot and extend it to year 2050
plt.plot(df['Year'], slope * df['Year'] + intercept, 'r', label='Best Fit Line')

# Plot a new line of best fit using the data from year 2000 through the most recent year
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(df_recent['Year'], slope_recent * df_recent['Year'] + intercept_recent, 'g', label='Best Fit Line (Since 2000)')

# Plot the projected sea level rise in 2050
plt.plot([df['Year'].iloc[-1], 2050], [slope_recent * df['Year'].iloc[-1] + intercept_recent, slope_recent * 2050 + intercept_recent], 'k--', label='Projected Rise in 2050')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()

# Save and return the image
plt.savefig('sea_level_rise.png')
plt.show()

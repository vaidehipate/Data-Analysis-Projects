import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# Create the overweight column in the df variable
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data in df_cat to split it by cardio
    df_cat = pd.DataFrame(df_cat.groupby(['variable', 'value', 'cardio'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

    # Convert the data into long format and create a chart
    fig = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Clean the data in the df_heat variable
df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) & 
    (df['height'] <= df['height'].quantile(0.975)) & 
    (df['weight'] >= df['weight'].quantile(0.025)) & 
    (df['weight'] <= df['weight'].quantile(0.975))
]

# Calculate the correlation matrix
corr = df_heat.corr()

# Generate a mask for the upper triangle
mask = (corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool)))

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(11, 9))

# Plot the correlation matrix
sns.heatmap(corr, annot=True, fmt='.1f', linewidths=.5, mask=mask, vmax=.3, center=0, square=True, cbar_kws={"shrink": .5})

# Do not modify the next two lines
fig.savefig('heatmap.png')
return fig

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Use Pandas to import the data from "fcc-forum-pageviews.csv" and set the index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset
df_clean = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]

# Create a draw_line_plot function that uses Matplotlib to draw a line chart
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df_clean.index, df_clean['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

# Create a draw_bar_plot function that draws a bar chart
def draw_bar_plot():
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    fig = df_bar.plot(kind='bar', figsize=(10, 8)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[calendar.month_name[i] for i 

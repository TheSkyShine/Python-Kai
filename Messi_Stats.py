import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Acquires data from csv using Pandas and puts wanted variables into lists
file = 'messi barca fixed.csv'
data = pd.read_csv(file, encoding='latin-1')

season = data.Season
matches_played = data.Matches_Played
goals_scored = data.Goals_scored
assists = data.Assists



# Counts the length of the variable for the x-axis (season) and creates an array that counts up to that value
x_indexes = np.arange(len(season))

# Desired width of our bars
width = 0.25

# Change the style of the plot design to make it look cool
plt.style.use('seaborn-colorblind')

# Plots bars. Notice that some bars are shifted left or right by the width, because if not, they'd overlay each other
plt.bar(x_indexes-width, matches_played, label='Matches Played',width=width)
plt.bar(x_indexes, goals_scored, label='Goals Scored',width=width)
plt.bar(x_indexes+width, assists, label='Assists',width=width)

# Changes x labels back to seasons and also adds attributes to them to make them readable
plt.xticks(ticks=x_indexes, labels=season, rotation=45, horizontalalignment='right')

# Adds legend and necessary info
plt.legend()

plt.title('Messi Stats from 2004-2020')
plt.xlabel('Season')

plt.grid(axis='x')
plt.tight_layout()






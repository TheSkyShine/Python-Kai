import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file = 'messi barca fixed.csv'
data = pd.read_csv(file, encoding='latin-1')

season = data.Season
matches_played = data.Matches_Played
goals_scored = data.Goals_scored
assists = data.Assists

x_indexes = np.arange(len(season))
width = 0.25

plt.style.use('seaborn-colorblind')

plt.bar(x_indexes-width, matches_played, label='Matches Played',width=width)
plt.bar(x_indexes, goals_scored, label='Goals Scored',width=width)
plt.bar(x_indexes+width, assists, label='Assists',width=width)

plt.xticks(ticks=x_indexes, labels=season, rotation=45, horizontalalignment='right')

plt.legend()

plt.title('Messi Stats from 2004-2020')
plt.xlabel('Season')

plt.grid(axis='y')
plt.rc('axes', axisbelow=False)
plt.tight_layout()






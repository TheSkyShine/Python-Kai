##################################
# Code Provided by Corey Schafer #
##################################

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Changes style of plot
plt.style.use('fivethirtyeight')

# Creates function to be called by FuncAnimation class. Reads .csv and seperates data into lists
def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

# clears axes. If not included, old plot will remain when new one gets added on top
    plt.cla()

# Plots the datasets
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()

# FuncAnimation class is called. plt.gcf() is get current figure, animate is the function to be called,
# and interval is how often to call said function
ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()

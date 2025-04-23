# Brittani Chandler
# graph for large cubes
# 4/22/2025

"""plot_colored_cubes.py

This script plots the first 5,000 cubic numbers using a scatter plot
with a pink-to-purple colormap on a dark background.
"""

import matplotlib.pyplot as plt
import numpy as np
from cubes import generate_cubes
from matplotlib.colors import LinearSegmentedColormap

x_vals = list(range(1, 5001))
y_vals = generate_cubes(5000)

# Define custom pink-to-purple colormap
colors = ["#ff69b4", "#cc33ff", "#8000ff"]  # pink → magenta → purple
pink_purple_cmap = LinearSegmentedColormap.from_list("PinkPurple", colors)

# Use dark background style
plt.style.use('dark_background')
fig, ax = plt.subplots()

# Create scatter plot
scatter = ax.scatter(x_vals, y_vals, c=y_vals, cmap=pink_purple_cmap, s=1)

# Set titles and labels
ax.set_title("Cubic Numbers (1–5000)", fontsize=20, color='white')
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(labelsize=12, colors='white')

plt.savefig("colored_cubes_plot.png", bbox_inches='tight')
plt.show()

# Brittani Chandler
# graph for small cubes
# 4/22/2025

"""plot_small_cubes.py

This script plots the first five cubic numbers using a line plot
with a dark background and an ombre gradient from pink to purple.
"""

import matplotlib.pyplot as plt
from cubes import generate_cubes

x_vals = list(range(1, 6))
y_vals = generate_cubes(5)

# Use dark background style
plt.style.use('dark_background')
fig, ax = plt.subplots()

# Plot line segments with pink to purple ombre
colors = ['#ff69b4', '#ff33cc', '#cc33ff', '#9933ff', '#8000ff']  # Gradient: pink to purple
for i in range(1, len(x_vals)):
    ax.plot(x_vals[i-1:i+1], y_vals[i-1:i+1], linewidth=3, color=colors[i])

# Set titles and labels
ax.set_title("Cubic Numbers (1–5)", fontsize=20, color='white')
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(labelsize=14, colors='white')

plt.savefig("small_cubes_plot.png", bbox_inches='tight')
plt.show()



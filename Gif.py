import Tests as t
import matplotlib
import numpy as np
import random
import time
import imageio
import os
from matplotlib.patches import Patch
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

N_values = np.linspace(1, 1000, 10)
M_values = np.linspace(1, 1000, 10)
X, Y = np.meshgrid(M_values, N_values)
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

colors = ['Reds', 'Purples', 'Oranges', 'Blues', 'Greens']
color_patches = []

for idx, (sort_name, sort_func) in enumerate(t.SORTING_ALG.items()):
    time_matrix = np.zeros((len(N_values), len(M_values)))

    for i, N in enumerate(N_values):
        for j, M in enumerate(M_values):
            numbers = [random.randint(1, int(M)) for _ in range(int(N))]

            start_time = time.time()
            sorted_numbers = sort_func(numbers)
            end_time = time.time()

            time_matrix[i, j] = end_time - start_time

    surf = ax.plot_surface(X, Y, time_matrix, cmap=colors[idx % len(colors)], edgecolor='none', alpha=0.5, label=sort_name)


ax.set_xlabel('Limit (M)')
ax.set_ylabel('Range (N)')
ax.set_zlabel('Time (s)')
ax.set_title('Sorting Algorithm Performance Comparison')

for idx, sort_name in enumerate(t.SORTING_ALG.keys()):
    cmap = plt.get_cmap(colors[idx % len(colors)])
    primary_color = cmap(0.5)
    patch = Patch(color=primary_color, label=sort_name)
    color_patches.append(patch)
ax.legend(handles=color_patches, loc="best")
angles = range(0, 102, 3)
filenames = []

for angle in angles:
    ax.view_init(30, angle)
    fig.canvas.draw()
    plt.pause(0.1)
    filename = f"frame_{angle}.png"
    fig.savefig(filename)
    filenames.append(filename)

reversed_filenames = filenames[::-1][1:-1]
filenames += reversed_filenames

with imageio.get_writer('sorting_algorithm_performance.gif', mode='I', duration=1, loop=0) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

for filename in set(filenames):
    os.remove(filename)

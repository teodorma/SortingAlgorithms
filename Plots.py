import Tests as t
import numpy as np
import random
import time
import matplotlib.pyplot as plt


def read_tests(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        tests = [(int(x), int(y)) for x, y in [line.split() for line in lines]]
    return tests


def plot_performance(Times_N, N_values, Times_M, M_values):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    for sort_name in t.sorting_algorithms:
        ax[0].plot(N_values, Times_N[sort_name], label=sort_name)
    ax[0].set_xlabel('Array Size (N)')
    ax[0].set_ylabel('Time (seconds)')
    ax[0].set_title('Performance by Array Size (N)')
    ax[0].legend()

    for sort_name in t.sorting_algorithms:
        ax[1].plot(M_values, Times_M[sort_name], label=sort_name)
    ax[1].set_xlabel('Maximum Value (M)')
    ax[1].set_title('Performance by Max Value (M)')
    ax[1].legend()

    plt.tight_layout()
    plt.show()


def plot_surfaces():
    N_values = np.linspace(1, 1000, 10)
    M_values = np.linspace(1, 1000, 10)
    colors = ['Reds', 'Purples', 'Oranges', 'Blues', 'Greens']

    for idx, (sort_name, sort_func) in enumerate(t.SORTING_ALG.items()):
        time_matrix = np.zeros((len(N_values), len(M_values)))

        for i, N in enumerate(N_values):
            for j, M in enumerate(M_values):
                numbers = [random.randint(1, int(M)) for _ in range(int(N))]

                start_time = time.time()
                sorted_array = sort_func(numbers)
                end_time = time.time()

                time_matrix[i, j] = end_time - start_time

        X, Y = np.meshgrid(M_values, N_values)
        fig = plt.figure(figsize=(14, 10))
        ax = fig.add_subplot(111, projection='3d')

        ax.plot_surface(X, Y, time_matrix, cmap=colors[idx % len(colors)], edgecolor='none', alpha=0.5)

        ax.set_xlabel('Limit (M)')
        ax.set_ylabel('Range (N)')
        ax.set_zlabel('Time (s)')
        ax.set_title('Performance of {}'.format(sort_name))

        plt.show()
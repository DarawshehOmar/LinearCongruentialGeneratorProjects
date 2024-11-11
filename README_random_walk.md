Description

This Python script simulates a random walk on a 15x15 grid using a Linear Congruential Generator (LCG) for generating pseudo-random directions. The random walk starts from the center of the grid, and the visit frequencies for each cell are tracked and visualized as a heatmap.

Features

Linear Congruential Generator (LCG): Generates a sequence of pseudo-random numbers to guide the random walk.

Random Walk Simulation: Simulates a random walk on a 15x15 grid with configurable number of steps.

Heatmap Visualization: Displays a heatmap showing the frequency of visits to each cell.

Requirements

Python 3

NumPy

Matplotlib



Parameters

size: Grid size (default is 15x15).

moves: Number of moves in the random walk (default is 1,000,000).

seed: Initial seed for the LCG.

a, c, m: Parameters for the LCG formula to generate pseudo-random numbers.

The output includes:

A text-based count of visits for each coordinate with non-zero visits.
A heatmap showing the frequency of visits across the grid.

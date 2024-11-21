# Random Walk Simulation on a Grid with LCG

This Python script simulates a random walk on a grid using the **Linear Congruential Generator (LCG)** for generating random directions. The walk is visualized through a heatmap that highlights the frequency of visits to each cell on the grid.

---

## Features

- **Linear Congruential Generator (LCG)**:
  - Generates pseudo-random numbers for determining whether to move and the direction of movement.
  - Parameters:
    - `a = 1664525`: Multiplier
    - `c = 1013904223`: Increment
    - `m = 2^31 - 1`: Modulus (prime number for better randomness).
- **Grid-Based Random Walk**:
  - Simulates a walk on a 15x15 grid by default.
  - Wraps around edges, creating a toroidal grid.
- **Visualization**:
  - Generates a heatmap showing the frequency of visits to each cell on the grid.

---

## Prerequisites

Ensure the following dependencies are installed:
- Python 3.x
- NumPy:
  ```bash
  pip install numpy


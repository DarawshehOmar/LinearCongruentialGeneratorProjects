# Random Movement Simulation on a Grid

This Python script simulates the movement of two points (`Point 1` and `Point 2`) on a grid using the Linear Congruential Generator (LCG) for random number generation. The two points can move independently or together with a configurable probability.

---

## Features

- **Random Direction Movement**: Uses an LCG to generate pseudo-random directions (`up`, `down`, `left`, `right`) for the points.
- **Grid Visualization**: Displays a real-time grid with updated positions of the points.
- **Movement Types**:
  - Points move together 80% of the time.
  - Points move independently 20% of the time.
- **Interactive Controls**: Users can continue or exit the simulation by pressing `Enter` or typing `q`.

---

## How It Works

### Random Movement
- **Linear Congruential Generator (LCG)**:
  - Formula: 
    ```
    X(n+1) = (a * X(n) + c) % m
    ```
  - Parameters:
    - `a = 1664525` (Multiplier)
    - `c = 1013904223` (Increment)
    - `m = 2^32` (Modulus)
    - `seed = 12345` (Initial Seed)
- **Direction Choices**:
  - `u`: Up
  - `d`: Down
  - `l`: Left
  - `r`: Right

### Visualization
- The grid is displayed using Matplotlib, with:
  - A **blue dot** representing `Point 1`.
  - A **red dot** representing `Point 2`.
- Grid size is 8x8 by default, but can be customized.

---

## Prerequisites

Ensure the following dependencies are installed:
- Python 3.x
- Matplotlib: Install it via pip:
  ```bash
  pip install matplotlib

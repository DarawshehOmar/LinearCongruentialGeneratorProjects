# Linear Congruential Generator (LCG) Random Walk Simulation

This Python script simulates two types of random walks based on the **Linear Congruential Generator (LCG)**. The positions are tracked and plotted using two distinct rules:
1. **Even/Odd Logic**: Movement is determined by whether the random number is even or odd.
2. **Half of Modulus Logic**: Movement is based on whether the random number is less than or greater than half of the modulus (`m`).

---

## Features

- **Random Walk Simulation**:
  - Tracks positions based on two rules:
    1. **Even/Odd Logic**: Move forward if the random number is odd; move back if even.
    2. **Half of Modulus Logic**: Move forward if the random number is greater than half of `m`; move back otherwise.
- **Dynamic Visualization**:
  - Generates two plots:
    1. Position vs. Steps (Even/Odd Logic).
    2. Position vs. Steps (Half of Modulus Logic).

---

## Prerequisites

Ensure the following dependencies are installed:
- Python 3.x
- Pylab (part of Matplotlib): Install it via:
  ```bash
  pip install matplotlib

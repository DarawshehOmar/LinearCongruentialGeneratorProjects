# Linear Congruential Generator (LCG) with Visualization

This Python script implements a **Linear Congruential Generator (LCG)** to generate pseudo-random numbers based on user-provided parameters. The script includes input validation and visualizes the generated sequence using `matplotlib`.

---

## Features

- **Input Validation**: Ensures the parameters `a`, `c`, and `m` meet the requirements of the LCG algorithm.
- **Period Detection**: Stops the sequence generation when repetition is detected, calculating the period.
- **Visualization**: Plots the generated random numbers against iterations for analysis.
- **Error Handling**: Handles invalid inputs gracefully and provides meaningful error messages.

---

## How It Works

The Linear Congruential Generator generates random numbers using the formula:

X(n+1) = (a * X(n) + c) % m

Where:
- `a`: Multiplier
- `c`: Increment
- `m`: Modulus
- `X₀`: Initial seed value




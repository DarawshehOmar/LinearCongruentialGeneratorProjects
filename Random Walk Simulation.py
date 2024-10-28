#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def linear_congruential_generator(seed, a, c, m):
    """Generates a sequence of pseudo-random numbers using Linear Congruential Generator (LCG)."""
    while True:
        seed = (a * seed + c) % m
        yield seed

def create_grid(size):
    """Creates a size x size grid initialized with zeros."""
    return np.zeros((size, size), dtype=int)

def simulate_random_walk(size, moves, seed, a, c, m):
    """Simulates a random walk on a grid using an LCG for random direction."""
    # Initialize starting position and visit count grid
    dot_position = (size // 2, size // 2)  # Start at the center of the grid
    counts = np.zeros((size, size), dtype=int)  # Visit count for each cell

    # Initialize the linear congruential generator
    lcg = linear_congruential_generator(seed, a, c, m)

    # Perform random walk
    for _ in range(moves):
        # Count the current position
        counts[dot_position[1], dot_position[0]] += 1

        # Generate random values to determine movement
        take_a_step = next(lcg) % 2  # Decide to move (0 or 1)
        direction = next(lcg) % 8  # Random direction (0-7)

        # Move the dot if take_a_step is 1
        if take_a_step == 1:
            dot_position = calculate_new_position(dot_position, direction, size)

    return counts

def calculate_new_position(position, direction, size):
    """Calculates the new position of the dot based on direction, wrapping around edges."""
    x, y = position
    if direction == 0:  # Up
        return (x, (y - 1) % size)
    elif direction == 1:  # Left
        return ((x - 1) % size, y)
    elif direction == 2:  # Down
        return (x, (y + 1) % size)
    elif direction == 3:  # Right
        return ((x + 1) % size, y)
    elif direction == 4:  # Up-left
        return ((x - 1) % size, (y - 1) % size)
    elif direction == 5:  # Up-right
        return ((x + 1) % size, (y - 1) % size)
    elif direction == 6:  # Down-left
        return ((x - 1) % size, (y + 1) % size)
    elif direction == 7:  # Down-right
        return ((x + 1) % size, (y + 1) % size)

def display_counts(counts):
    """Displays visit counts for each cell in the grid that has been visited."""
    size = len(counts)
    print("Counts of visits to each coordinate:")
    for y in range(size):
        for x in range(size):
            if counts[y, x] > 0:
                print(f"Probability of ({x}, {y}) is {counts[y, x]}")

def plot_heatmap(counts):
    """Plots a heatmap of visit frequencies on the grid."""
    size = len(counts)
    plt.figure(figsize=(10, 8))
    plt.imshow(counts, cmap='YlGnBu', interpolation='nearest')
    plt.colorbar(label='Count of Visits')
    plt.title('Heatmap of Dot Visits (15x15 Grid)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    # Add counts on the heatmap
    for y in range(size):
        for x in range(size):
            plt.text(x, y, counts[y, x], ha='center', va='center', color='black')
    plt.show()

def main():
    # Parameters
    size = 15             # Grid size
    moves = 1000000       # Number of moves in the random walk
    seed = 42             # Initial seed for the LCG
    a = 1664525           # LCG multiplier
    c = 1013904223        # LCG increment
    m = 2**31 - 1         # LCG modulus (prime number)

    # Run the simulation
    counts = simulate_random_walk(size, moves, seed, a, c, m)

    # Display results
    display_counts(counts)
    plot_heatmap(counts)

if __name__ == "__main__":
    main()

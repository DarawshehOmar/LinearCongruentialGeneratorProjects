import matplotlib.pyplot as plt

# Initialize the grid size
grid_size = 8
x1, y1 = 4, 4
x2, y2 = x1, y1

# LCG parameters
lcg_a = 1664525
lcg_c = 1013904223
lcg_m = 2**32
lcg_seed = 12345

# LCG function for generating random numbers
def lcg():
    global lcg_seed
    lcg_seed = (lcg_a * lcg_seed + lcg_c) % lcg_m
    return lcg_seed

# Function to get a random direction based on LCG output
def random_direction():
    directions = ['u', 'd', 'l', 'r']
    return directions[lcg() % 4]

# Set up the plot initially
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-0.5, grid_size - 0.5)
ax.set_ylim(-0.5, grid_size - 0.5)
ax.invert_yaxis()  # Invert y-axis for traditional grid orientation

# Draw grid lines and labels once
ax.grid(True)
ax.set_xticks(range(grid_size))
ax.set_yticks(range(grid_size))

# Initialize the points
point1, = ax.plot(x1, y1, 'bo', markersize=15, label="Point 1")  # Blue dot for Point 1
point2, = ax.plot(x2, y2, 'ro', markersize=15, label="Point 2")  # Red dot for Point 2
ax.legend()

# Function to update points' positions on the grid
def update_positions(x1, y1, x2, y2):
    point1.set_data(x1, y1)
    point2.set_data(x2, y2)
    plt.pause(0.1)  # Small pause to update the display

# Display initial positions
update_positions(x1, y1, x2, y2)

# Movement loop
while True:
    stay_together = lcg() % 100 < 80  # 80% chance to move together to the same position

    if stay_together:
        direction = random_direction()
        if direction == 'u' and y1 > 0:
            y1 -= 1
            y2 -= 1
        elif direction == 'd' and y1 < grid_size - 1:
            y1 += 1
            y2 += 1
        elif direction == 'l' and x1 > 0:
            x1 -= 1
            x2 -= 1
        elif direction == 'r' and x1 < grid_size - 1:
            x1 += 1
            x2 += 1
    else:
        # Move each point independently
        for _ in range(2):  # Repeat for each point
            direction = random_direction()
            if direction == 'u' and y1 > 0:
                y1 -= 1
            elif direction == 'd' and y1 < grid_size - 1:
                y1 += 1
            elif direction == 'l' and x1 > 0:
                x1 -= 1
            elif direction == 'r' and x1 < grid_size - 1:
                x1 += 1

        for _ in range(2):  # Repeat for the second point
            direction = random_direction()
            if direction == 'u' and y2 > 0:
                y2 -= 1
            elif direction == 'd' and y2 < grid_size - 1:
                y2 += 1
            elif direction == 'l' and x2 > 0:
                x2 -= 1
            elif direction == 'r' and x2 < grid_size - 1:
                x2 += 1

    update_positions(x1, y1, x2, y2)

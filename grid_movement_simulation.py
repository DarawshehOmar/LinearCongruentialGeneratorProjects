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
        # Move both points together in the same direction
        move = random_direction()
        if move == 'u':
            y1 = y2 = (y1 - 1) % grid_size
        elif move == 'l':
            x1 = x2 = (x1 - 1) % grid_size
        elif move == 'd':
            y1 = y2 = (y1 + 1) % grid_size
        elif move == 'r':
            x1 = x2 = (x1 + 1) % grid_size
    else:
        # Move each point separately
        move1 = random_direction()
        move2 = random_direction()

        # Update Point 1 position
        if move1 == 'u':
            y1 = (y1 - 1) % grid_size
        elif move1 == 'l':
            x1 = (x1 - 1) % grid_size
        elif move1 == 'd':
            y1 = (y1 + 1) % grid_size
        elif move1 == 'r':
            x1 = (x1 + 1) % grid_size

        # Update Point 2 position
        if move2 == 'u':
            y2 = (y2 - 1) % grid_size
        elif move2 == 'l':
            x2 = (x2 - 1) % grid_size
        elif move2 == 'd':
            y2 = (y2 + 1) % grid_size
        elif move2 == 'r':
            x2 = (x2 + 1) % grid_size

    # Update the positions on the grid
    update_positions(x1, y1, x2, y2)

    # User prompt to continue or quit
    cont = input("Press Enter to move points, or 'q' to quit: ")
    if cont.lower() == 'q':
        print("Exiting the grid.")
        break

plt.close(fig)  # Close the plot when done

# Define LCG parameters
a = 1664525        # Multiplier
c = 1013904223     # Increment
m = 2**32          # Modulus
seed = 42          # Initial seed

# Function to generate a pseudo-random integer using LCG
def lcg():
    global seed
    seed = (a * seed + c) % m
    return seed

# File path for the XYZ output
file_path = "carbonyl_100_moves_lcg.xyz"

# Function to generate 100 random positions for C and O within an 8x8 grid using LCG
def generate_lcg_positions(grid_size=8, num_moves=100):
    positions = []
    for _ in range(num_moves):
        # Random position for C with z=1 using LCG
        c_x = lcg() % grid_size
        c_y = lcg() % grid_size
        c_z = 1

        # Random position for O with z randomly set to 1 or 2 using LCG
        o_x = lcg() % grid_size
        o_y = lcg() % grid_size
        o_z = 1 if lcg() % 2 == 0 else 2

        positions.append((f"C {c_x} {c_y} {c_z}", f"O {o_x} {o_y} {o_z}"))
    return positions

# Fixed Cu grid for 8x8 arrangement
cu_positions = [f"Cu {x} {y} 0" for x in range(8) for y in range(8)]

# Generate 100 random positions for C and O atoms using LCG
random_positions = generate_lcg_positions(num_moves=100)

# Write to the XYZ file with 100 frames
with open(file_path, "w") as file:
    for c_position, o_position in random_positions:
        # Write the number of atoms (64 Cu + 2 moving atoms C and O)
        file.write("66\n")
        file.write("Cu grid with randomly moving C and O atoms (LCG)\n")
        
        # Write Cu grid positions
        for cu in cu_positions:
            file.write(f"{cu}\n")
        
        # Write current C and O positions
        file.write(f"{c_position}\n")
        file.write(f"{o_position}\n")

print(f"File '{file_path}' created successfully with 100 frames for C and O movements using LCG.")

#!/usr/bin/python3
import pylab

def generate_random_number(a, c, m, x0):
    # Generate the next random number using the LCG formula.
    return (a * x0 + c) % m

def main():
    try:
        # Get LCG parameters and number of iterations from the user
        x = int(input("Enter the seed value (x0): "))
        a = int(input("Enter the multiplier (a): "))
        c = int(input("Enter the increment (c): "))
        m = int(input("Enter the modulus (m): "))
        num_iterations = int(input("Enter the number of iterations: "))

        # Initialize variables for position tracking
        position_even_odd = 0  # Position using even/odd logic
        position_half = 0      # Position using half of m logic
        steps = []             # List to store step counts
        positions_even_odd = []  # List to store positions for even/odd
        positions_half = []    # List to store positions for half of m

        for i in range(num_iterations):
            # Generate the next random number
            x = generate_random_number(a, c, m, x)
            
            # Update position based on even/odd logic
            if x % 2 == 1:  # Check if x is odd
                position_even_odd += 1  # Move forward if x is odd
            else:
                position_even_odd -= 1  # Move back if x is even

            # Update position based on half of m logic
            if x <= (m - 1) / 2:
                position_half -= 1  # Move back if number is <= half of m
            else:
                position_half += 1  # Move forward if number is > half of m

            # Store the step and position
            steps.append(i)
            positions_even_odd.append(position_even_odd)
            positions_half.append(position_half)

        # Create two plots
        pylab.figure(figsize=(12, 6))

        pylab.subplot(1, 2, 1)
        pylab.plot(steps, positions_even_odd, 'b-')
        pylab.title('Position vs. Steps (Even/Odd Logic)')
        pylab.xlabel('Step')
        pylab.ylabel('Position')
        pylab.grid()

        pylab.subplot(1, 2, 2)
        pylab.plot(steps, positions_half, 'r-')
        pylab.title('Position vs. Steps (Half of m Logic)')
        pylab.xlabel('Step')
        pylab.ylabel('Position')
        pylab.grid()

        pylab.tight_layout()
        pylab.show()

    except ValueError as error:
        print(f"Error: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

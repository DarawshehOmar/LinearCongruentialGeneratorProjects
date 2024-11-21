import matplotlib.pyplot as plt
def generate_random_number(a, c, m, x0):
    return (a * x0 + c) % m

def validate_parameters(a, c, m):
    if m <= 1:
        raise ValueError("Modulus (m) must be greater than 1.")
    if a <= 0 or c < 0 or m <= 0:
        raise ValueError("Parameters 'a', 'c', and 'm' must be positive integers.")

def main():
    try:
        a = int(input("Enter the multiplier (a): "))
        c = int(input("Enter the increment (c): "))
        m = int(input("Enter the modulus (m): "))
        x0 = int(input("Enter the initial seed value (X0): "))
        num_iterations = int(input("How many iterations would you like to run? "))

        validate_parameters(a, c, m)

        random_numbers = []
        iterations = []
        seen_numbers = set()
        period = 0

        for i in range(num_iterations):
            x0 = generate_random_number(a, c, m, x0)
            if x0 in seen_numbers:
                print("Repetition detected, stopping sequence.")
                break
            seen_numbers.add(x0)
            random_numbers.append(x0)
            iterations.append(i)
            period += 1
            print(f"Random number {i + 1}: {x0}")

        print(f"The period is: {period}")

        # Plot the generated random numbers
        plt.plot(iterations, random_numbers, "b.")
        plt.title(f"LCG Generated Random Numbers (Period: {period})")
        plt.xlabel("Iteration")
        plt.ylabel("Random Number")
        plt.xlim(left=0)  # Ensure the x-axis starts at 0
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except ValueError as error:
        print(f"Error: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

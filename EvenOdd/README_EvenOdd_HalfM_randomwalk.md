Description

This project simulates a random walk by generating a sequence of numbers with an LCG and updating two separate positional variables based on distinct rules:

Even/Odd Logic: Moves the position forward if the generated number is odd and backward if it’s even.
Half of m Logic: Moves the position based on whether the generated number is less than or greater than half of the modulus (m).
The script then plots the results, providing a visual comparison of the two different tracking logics.

Features

Generates a sequence of pseudo-random numbers using an LCG.
Tracks position changes based on Even/Odd logic and Half of m logic.
Visualizes the position over time for both tracking methods.

Requirements

Python 3.x

pylab (usually included with matplotlib)


Usage

The program will prompt you to enter the following values:
Seed (x0): Initial value for the random number sequence.
Multiplier (a): Multiplier parameter for the LCG.
Increment (c): Increment parameter for the LCG.
Modulus (m): Modulus parameter for the LCG.
Number of Iterations: Total steps to simulate in the random walk.


The script will generate two plots:
Position over time based on Even/Odd logic.
Position over time based on Half of m logic.

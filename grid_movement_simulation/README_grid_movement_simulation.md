Grid Movement Simulation

This Python script simulates the movement of two points on an 8x8 grid using a Linear Congruential Generator (LCG) to generate pseudo-random directions. The points have an 80% chance of moving together to the same position, and they are visualized in real-time on the grid.

Features

Random Point Movement: Each point has a chance to move in random directions (up, down, left, right) based on the LCG output.

Synchronized Movement: With an 80% probability, both points move to the same position; otherwise, they move independently.

Real-time Visualization: The points are updated dynamically on the grid using Matplotlib, with "Point 1" in blue and "Point 2" in red.

Code Explanation LCG (Linear Congruential Generator):

Generates random numbers using the LCG algorithm to determine the movement direction.

Random Direction Function: Maps the LCG output to four possible directions ('up', 'down', 'left', 'right').

Update Positions: Updates the positions of the points on the grid and redraws them.

Movement Loop: Continuously moves the points, with an 80% chance for synchronized movement.

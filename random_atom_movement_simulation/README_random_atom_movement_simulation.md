# LCG-Random-Carbonyl-on-Grid

A Python script to simulate the random movement of Carbon (C) and Oxygen (O) atoms (carbonyl group) on a fixed 8x8 Copper (Cu) atom grid using a Linear Congruential Generator (LCG). The simulation generates an XYZ file that can be visualized with molecular modeling tools.

## Features
- **Random Atom Positions:** Uses LCG for pseudorandom positioning of C and O atoms.
- **Fixed Copper Grid:** Creates a static 8x8 grid of Cu atoms.
- **XYZ File Format:** Outputs a molecular simulation file compatible with visualization tools.
- **Simulation Frames:** Generates 100 frames of atomic positions.

## File Structure
- `simulation.py`: The main Python script for the simulation.
- `carbonyl_100_moves_lcg.xyz`: The output file containing the simulation frames.

## Output File Details
The generated XYZ file contains:

First Line: Total number of atoms (64 Cu + 2 moving atoms = 66).

Second Line: A description of the frame.

Remaining Lines: Atomic positions in the format Element x y z.


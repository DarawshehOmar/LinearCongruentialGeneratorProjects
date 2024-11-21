# Random Atom Position Generation Using LCG

This Python script generates random positions for `C` (Carbon) and `O` (Oxygen) atoms within an 8x8 grid using the Linear Congruential Generator (LCG). The positions are written to an XYZ file format, including a fixed grid of `Cu` (Copper) atoms.

---

## Features

- **Linear Congruential Generator (LCG)**:
  - Generates pseudo-random numbers for atom positions.
  - Parameters:
    - `a = 1664525`: Multiplier
    - `c = 1013904223`: Increment
    - `m = 2^32`: Modulus
    - `seed = 42`: Initial seed for repeatable results.

- **XYZ File Output**:
  - Generates 100 frames with:
    - 64 fixed positions for `Cu` atoms.
    - 1 `C` atom with a fixed `z`-coordinate of `1`.
    - 1 `O` atom with a `z`-coordinate randomly set to `1` or `2`.

---

## Prerequisites

Ensure the following dependencies are installed:
- Python 3.x

---

## Usage

1. Clone or download the script.
2. Run the script:
   ```bash
   python script_name.py
3. The script generates an XYZ file named carbonyl_100_moves_lcg.xyz containing:
100 frames of atomic positions.

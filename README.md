# betti

**betti** is a Python library for topological data analysis (TDA) using a fast Julia backend.  
It computes persistence diagrams and Betti numbers from point clouds or high-dimensional datasets.

---

## Features

- Compute persistence diagrams and Betti numbers from point clouds
- Build Vietoris–Rips complexes using Julia (`Eirene.jl`)
- Plot persistence diagrams and barcodes with Matplotlib
- Fully modular, pip-installable, production-ready

---

## Installation

pip install .

> Make sure Julia is installed and `pyjulia` is available in Python.

---

## Providing Data

**betti** does not fetch data automatically. All input data must be provided by the user. Supported formats:

### 1. NumPy arrays (most common)

import numpy as np
import betti

# Create a random 3D point cloud
points = np.random.rand(100, 3)

# Compute persistence
diagram = betti.compute_persistence(points)
betti.plot_diagram(diagram)
betti.plot_barcode(diagram)

### 2. CSV files

import pandas as pd
import betti

# Load points from a CSV file
# Each row = one point, columns = dimensions
df = pd.read_csv("points.csv")
points = df.to_numpy()

diagram = betti.compute_persistence(points)
betti.plot_diagram(diagram)
betti.plot_barcode(diagram)

### 3. pandas DataFrames

# If you already have a DataFrame with coordinates
points = df[['x','y','z']].to_numpy()
diagram = betti.compute_persistence(points)

---

## Notes on Data

- The input must be a numeric array of shape `(n_points, n_dimensions)`.  
- Each row corresponds to a single point in space.  
- Dimensions can be 2D, 3D, or higher depending on your dataset.  
- betti does not generate or download datasets; all data must be supplied by the user.

---

## Backend

- Computation is performed in Julia using modular code:
  - `Complexes.jl` builds Vietoris–Rips complexes
  - `Homology.jl` computes Betti numbers and persistence diagrams
  - `Core.jl` ties the workflow together
- Python calls the Julia backend via `PyJulia` using `_julia_loader.py`.

---

## License

MIT License

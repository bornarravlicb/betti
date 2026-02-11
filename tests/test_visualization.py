import numpy as np
from betti.visualization import plot_diagram, plot_barcode
from betti.core import compute_persistence

def test_plot_functions():
    points = np.random.rand(5, 2)
    diagram = compute_persistence(points)
    plot_diagram(diagram)
    plot_barcode(diagram)

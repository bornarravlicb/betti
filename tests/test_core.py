import numpy as np
from betti.core import compute_persistence

def test_persistence_output_shape():
    points = np.random.rand(10, 3)
    diagram = compute_persistence(points)
    assert isinstance(diagram, list)
    for pair in diagram:
        assert len(pair) == 2

from ._julia_loader import load_julia

Main = load_julia()

def compute_persistence(points):
    return Main.Core.compute_persistence(points)

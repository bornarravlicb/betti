import os
from julia import Julia
from julia import Main

_julia_initialized = False

def load_julia():
    global _julia_initialized
    if _julia_initialized:
        return Main

    Julia(compiled_modules=False)

    base_dir = os.path.dirname(__file__)
    julia_dir = os.path.join(base_dir, "../julia")

    Main.include(os.path.join(julia_dir, "complexes.jl"))
    Main.include(os.path.join(julia_dir, "homology.jl"))
    Main.include(os.path.join(julia_dir, "core.jl"))

    _julia_initialized = True
    return Main

module Core

export compute_persistence

using Complexes
using Homology

function compute_persistence(points::AbstractMatrix)
    pts = convert(Matrix{Float64}, points)
    complex = build_vr_complex(pts, maxdim=2)
    diagram = compute_homology(complex)
    return diagram
end

end


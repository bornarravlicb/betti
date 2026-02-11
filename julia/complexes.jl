module Complexes

export build_vr_complex

using Eirene

function build_vr_complex(points::AbstractMatrix; maxdim::Int=2)
    pts = convert(Matrix{Float64}, points)
    ph = eirene(pts, model="vr", maxdim=maxdim)
    return ph
end

end

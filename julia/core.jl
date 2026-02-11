using Eirene

function compute_persistence(points::AbstractMatrix)
    pts = convert(Matrix{Float64}, points)
    ph = eirene(pts, model="vr", maxdim=2)
    diagram = ph["dgms"]
    result = []
    for dgm in diagram
        for pair in dgm
            push!(result, (pair[1], pair[2]))
        end
    end
    return result
end

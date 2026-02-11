module Homology

export compute_homology

function compute_homology(ph)
    diagram = ph["dgms"]
    result = []
    for dgm in diagram
        for pair in dgm
            push!(result, (pair[1], pair[2]))
        end
    end
    return result
end

end

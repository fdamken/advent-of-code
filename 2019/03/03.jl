using LinearAlgebra
using Printf



wires = []
for line in readlines("input.txt")
    push!(wires, map(x -> (x[1], parse(Int, x[2:end])), split(line, ",")))
end
wire1moves = wires[1]
wire2moves = wires[2]


function calculatePositions(moves)
    positions = [(0, 0)]
    for move in moves
        (x, y) = positions[end]
        action = move[1]
        fields = move[2]
        if action == 'U'
            y += fields
        elseif action == 'D'
            y -= fields
        elseif action == 'L'
            x -= fields
        elseif action == 'R'
            x += fields
        else
            error("Impossible move!")
        end
        push!(positions, (x, y))
    end
    return positions
end

wire1 = calculatePositions(wire1moves)
wire2 = calculatePositions(wire2moves)

steps1 = 0
crossings = []
for i in 2:length(wire1)
    global steps1

    (x0, y0) = wire1[i - 1]
    (x1, y1) = wire1[i]
    steps1 += abs(x0 - x1) + abs(y0 - y1)
    steps2 = 0
    for j in 2:length(wire2)
        (X0, Y0) = wire2[j - 1]
        (X1, Y1) = wire2[j]
        steps2 += abs(X0 - X1) + abs(Y0 - Y1)
        if (x0 == x1) && (Y0 == Y1) && (min(y0, y1) <= Y0 <= max(y0, y1)) && (min(X0, X1) <= x0 <= max(X0, X1))
            # Moving over y-axis.
            if x0 == Y0 == 0
                continue
            end
            push!(crossings, ([x0, Y0], steps1 - abs(y1 - Y1), steps2 - abs(x1 - X1)))
        elseif (y0 == y1) && (X0 == X1) && (min(x0, x1) <= X0 <= max(x0, x1)) && (min(Y0, Y1) <= y0 <= max(Y0, Y1))
            # Moving over x-axis.
            if X0 == y0 == 0
                continue
            end
            push!(crossings, ([X0, y0], steps1 - abs(x1 - X1), steps2 - abs(y1 - Y1)))
        end
    end
end


manhattenDistance(x) = norm(x, 1)
minimumDistance = min(map(x -> norm(x[1], 1), crossings)...)
println("Day 3, Part 1: ", minimumDistance)

minSteps = min(map(x -> x[2] + x[3], crossings)...)
println("Day 3, Part 2: ", minSteps)

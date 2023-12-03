using DelimitedFiles



input = readdlm("input.txt")


function calcFuel(mass)
    fuel = floor(mass / 3) - 2
    if fuel <= 0
        return 0
    else 
        return fuel + calcFuel(fuel)
    end
end


println("Day 01, Part 1: ", sum(map(x -> floor(x / 3) - 2, input)))

println("Day 01, Part 2: ", sum(map(x -> calcFuel(x), input)))

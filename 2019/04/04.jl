input = "178416-676461"


inputSplit = split(input, "-")
from = parse(Int, inputSplit[1])
to = parse(Int, inputSplit[2])
passwordRange = from:to

cnt1 = 0
cnt2 = 0
for password in from:to
    global cnt1, cnt2

    i = 1
    increasing = true
    hasAdjacentNumbers = false
    hasExactAdjacentNumbers = false
    repeatCount = 1
    previous = -Inf
    previousPrevious = nothing
    for char in string(password)
        char = parse(Int, char)

        if char < previous
            increasing = false
            break
        end

        previousRepeatCount = repeatCount
        if char == previous
            repeatCount += 1
        else
            repeatCount = 1
        end

        if repeatCount == 2
            hasAdjacentNumbers = true
        end

        if repeatCount == 1 && previousRepeatCount == 2 || repeatCount == 2 && length(string(password)) == i
            hasExactAdjacentNumbers = true
        end

        previousPrevious = previous
        previous = char

        i += 1
    end

    if increasing && hasAdjacentNumbers
        cnt1 += 1
    end

    if increasing && hasExactAdjacentNumbers
        cnt2 += 1
    end
end


println("Day 04, Part 1: ", cnt1)
println("Day 04, Part 2: ", cnt2)

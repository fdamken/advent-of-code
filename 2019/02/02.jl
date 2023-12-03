using DelimitedFiles



input = readdlm("input.txt", ',', Int32)
# Fix the 1202 program alarm.
input[1 + 1] = 12
input[2 + 1] = 2


function run!(memory, pc = 1)
    opcode = memory[pc]
    if opcode == 1
        arg1 = memory[memory[pc + 1] + 1]
        arg2 = memory[memory[pc + 2] + 1]
        resultpos = memory[pc + 3]
        memory[resultpos + 1] = arg1 + arg2
        pc += 4
    elseif opcode == 2
        arg1 = memory[memory[pc + 1] + 1]
        arg2 = memory[memory[pc + 2] + 1]
        resultpos = memory[pc + 3]
        memory[resultpos + 1] = arg1 * arg2
        pc += 4
    elseif opcode == 99
        return
    else
        println("Something went wrong!")
        return
    end
    run!(memory, pc)
end


# Run the program.
program = copy(input)
run!(program)
output = program[0 + 1]
println("Day 02, Part 1: ", output)


# Bruteforce to find the input with the output 19690720.
for noun in 0:99
    for verb in 0:99
        program = copy(input)
        program[1 + 1] = noun
        program[2 + 1] = verb
        run!(program)
        output = program[0 + 1]
        if output == 19690720
            println("Day 02, Part 2: ", 100noun + verb)
        end
    end
end

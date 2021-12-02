def read_instructions():
    file_name = "Data/day2.txt"
    file = open(file_name, "r")
    instructions = []
    
    for line in file:
        line = line.strip("\n").split()
        line[1] = int(line[1])
        instructions.append(line)
        
    return instructions

def find_position(instructions):
    pos = [0, 0]
    
    for instruction in instructions:
        if instruction[0] == "forward":
            pos[0] += instruction[1]
        elif instruction[0] == "down":
            pos[1] += instruction[1]
        elif instruction[0] == "up":
            pos[1] -= instruction[1]

    print(f"Part one: {pos[0]*pos[1]}")
    
def aim_position(instructions):
    pos = [0, 0]
    aim = 0
    
    for instruction in instructions:
        if instruction[0] == "forward":
            pos[0] += instruction[1]
            pos[1] += instruction[1]*aim
        elif instruction[0] == "down":
            aim += instruction[1]
        elif instruction[0] == "up":
            aim -= instruction[1]

    print(f"Part two: {pos[0]*pos[1]}")
    
if __name__ == "__main__":
    instructions = read_instructions()
    find_position(instructions)
    aim_position(instructions)
    
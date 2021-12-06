import numpy as np

def read_vents():
    file_name = "Data/day5.txt"
    file = open(file_name, "r")
    vents = []
    
    for line in file:
        line = line.replace(" -> ", " ").replace(",", " ").split()
        line = list(map(int, line))
        vents.append(line)
        
    return vents

def find_overlaps(vents):
    grid = np.zeros([1000, 1000], dtype=int)
    
    for line in vents:
        if line[0] == line[2]:
            start = min(line[1], line[3])
            end = max(line[1], line[3])
            grid[line[0], start:end+1] += 1
        elif line[1] == line[3]:
            start = min(line[0], line[2])
            end = max(line[0], line[2])
            grid[start:end+1, line[1]] += 1
            
    print(f"Part one: {sum(sum(grid >= 2))}")
    
def diagonal_overlaps(vents):
    grid = np.zeros([1000, 1000], dtype=int)
    
    for line in vents:
        if line[0] == line[2]:
            start = min(line[1], line[3])
            end = max(line[1], line[3])
            grid[line[0], start:end+1] += 1
        elif line[1] == line[3]:
            start = min(line[0], line[2])
            end = max(line[0], line[2])
            grid[start:end+1, line[1]] += 1
        else:
            for i, j in zip(np.linspace(line[0], line[2], abs(line[2]-line[0])+1, dtype=int),
                            np.linspace(line[1], line[3], abs(line[3]-line[1])+1, dtype=int)):
                grid[i, j] += 1
                
    print(f"Part two: {sum(sum(grid >= 2))}")
        
if __name__ == "__main__":
    vents = read_vents()
    find_overlaps(vents)
    diagonal_overlaps(vents)
    
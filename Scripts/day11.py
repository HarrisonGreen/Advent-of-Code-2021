import numpy as np

def read_energy_levels():
    file_name = "Data/day11.txt"
    file = open(file_name, "r")
    levels = np.zeros([10, 10], dtype=int)
    
    for row, line in enumerate(file):
        line = line.strip("\n")
        
        for col, num in enumerate(line):
            levels[row, col] = num
        
    return levels

def simulate_steps(levels):
    flashes = 0
    t = 0
    
    while True:
        t += 1
        flashed = set()
        new_flashed = set()
        levels += 1
        
        for i in range(10):
            for j in range(10):
                if levels[i, j] > 9:
                    new_flashed.add((i, j))
                    
        while new_flashed:
                    
            for octopus in new_flashed:
                neighbours = get_neighbours(octopus)
                for neighbour in neighbours:
                    levels[neighbour] += 1
                    
            flashed = flashed.union(new_flashed)
            new_flashed = set()
                    
            for i in range(10):
                for j in range(10):
                    if levels[i, j] > 9 and (i, j) not in flashed:
                        new_flashed.add((i, j))
                        
        for i in range(10):
            for j in range(10):
                if levels[i, j] > 9:
                    levels[i, j] = 0
                        
        flashes += len(flashed)
        if t == 100:
            flash_count = flashes
        if len(flashed) == 100:
            return t, flash_count
    
def get_neighbours(pos):
    i = pos[0]
    j = pos[1]
    neighbours = []
    
    if i != 0:
        neighbours.append((i-1, j))
    if i != 9:
        neighbours.append((i+1, j))
    if j != 0:
        neighbours.append((i, j-1))
    if j != 9:
        neighbours.append((i, j+1))
    if i != 0 and j != 0:
        neighbours.append((i-1, j-1))
    if i != 0 and j != 9:
        neighbours.append((i-1, j+1))
    if i != 9 and j != 0:
        neighbours.append((i+1, j-1))
    if i != 9 and j != 9:
        neighbours.append((i+1, j+1))
        
    return neighbours

if __name__ == "__main__":
    energy_levels = read_energy_levels()
    sync_time, flashes = simulate_steps(energy_levels)
    print(f"Part one: {flashes}")
    print(f"Part two: {sync_time}")
    
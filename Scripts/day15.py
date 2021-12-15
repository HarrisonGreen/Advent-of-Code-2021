import numpy as np

def read_risk_levels():
    file_name = "Data/day15.txt"
    file = open(file_name, "r")
    
    for row, line in enumerate(file):
        line = line.strip("\n")
        
        if row == 0:
            dim = len(line)
            risk_levels = np.zeros([dim, dim], dtype = int)
            
        for col, num in enumerate(line):
            risk_levels[row, col] = num
        
    return risk_levels, dim

def least_risky_path(risk_levels, dim):
    path_risk = np.zeros([dim, dim], dtype = int)
    path_risk += 1000000
    path_risk[0, 0] = 0
    
    processed = {(i, j): False for i in range(dim) for j in range(dim)}
    to_process = {0: {(0, 0)}}
    
    while to_process:
        positions = to_process.pop(min(to_process.keys()))
        
        for x, y in positions:
            if processed[(x, y)]:
                continue
            
            processed[(x, y)] = True
            
            if x != 0 and not processed[(x - 1, y)]:
                path_risk[(x - 1, y)] = min(path_risk[(x - 1, y)],
                                            path_risk[(x, y)] + risk_levels[(x - 1, y)])
                to_process[path_risk[(x - 1, y)]] = to_process.get(path_risk[(x - 1, y)], set())
                to_process[path_risk[(x - 1, y)]].add((x - 1, y))
                
            if x != dim - 1 and not processed[(x + 1, y)]:
                path_risk[(x + 1, y)] = min(path_risk[(x + 1, y)],
                                            path_risk[(x, y)] + risk_levels[(x + 1, y)])
                to_process[path_risk[(x + 1, y)]] = to_process.get(path_risk[(x + 1, y)], set())
                to_process[path_risk[(x + 1, y)]].add((x + 1, y))
                
            if y != 0 and not processed[(x, y - 1)]:
                path_risk[(x, y - 1)] = min(path_risk[(x, y - 1)],
                                            path_risk[(x, y)] + risk_levels[(x, y - 1)])
                to_process[path_risk[(x, y - 1)]] = to_process.get(path_risk[(x, y - 1)], set())
                to_process[path_risk[(x, y - 1)]].add((x, y - 1))
                
            if y != dim - 1 and not processed[(x, y + 1)]:
                path_risk[(x, y + 1)] = min(path_risk[(x, y + 1)],
                                            path_risk[(x, y)] + risk_levels[(x, y + 1)])
                to_process[path_risk[(x, y + 1)]] = to_process.get(path_risk[(x, y + 1)], set())
                to_process[path_risk[(x, y + 1)]].add((x, y + 1))
    
    return path_risk[dim - 1, dim - 1]
    
def tile_cave(risk_levels, dim):
    new_levels = np.zeros([5 * dim, 5 * dim], dtype = int)
    new_levels[:dim, :dim] = risk_levels
    
    for i in range(1, 5):
        new_levels[i * dim:(i + 1) * dim, :dim] = (new_levels[(i - 1) * dim:i * dim, :dim] % 9) + 1
        
    for i in range(5):
        for j in range(1, 5):
            new_levels[i * dim:(i + 1) * dim, j * dim:(j + 1) * dim] = (new_levels[i * dim:(i + 1) * dim, (j - 1) * dim:j * dim] % 9) + 1
            
    return new_levels
        
if __name__ == "__main__":
    risk_levels, dim = read_risk_levels()
    print(f"Part one: {least_risky_path(risk_levels, dim)}")
    risk_levels = tile_cave(risk_levels, dim)
    print(f"Part two: {least_risky_path(risk_levels, 5 * dim)}")
    
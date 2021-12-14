import numpy as np

def read_heights():
    file_name = "Data/day9.txt"
    file = open(file_name, "r")

    for row, line in enumerate(file):
        line = line.strip("\n")

        if row == 0:
            heights = np.zeros([len(line), len(line)], dtype=int)

        for i in range(len(line)):
            heights[row, i] = line[i]

    return heights, len(line)

def risk_levels(heights, dim):
    total = 0
    low_points = []

    for i in range(dim):
        for j in range(dim):
            neighbour_heights = set(heights[pos] for pos in find_neighbours(i, j, dim))
            if heights[i, j] < min(neighbour_heights):
                total += heights[i, j] + 1
                low_points.append((i, j))

    print(f"Part one: {total}")
    return low_points

def find_neighbours(x, y, dim):
    neighbours = []
    if x != 0:
        neighbours.append((x-1, y))
    if x!= dim-1:
        neighbours.append((x+1, y))
    if y != 0:
        neighbours.append((x, y-1))
    if y != dim-1:
        neighbours.append((x, y+1))
    return neighbours

def find_basins(heights, dim, low_points):
    basins = {point: 0 for point in low_points}
    processed = {(i, j): False for i in range(dim) for j in range(dim)}
    to_process = {point: point for point in low_points}
    
    for point in low_points:
        processed[point] = True

    while to_process:
        to_add = {}

        for pos, parent in to_process.items():
            basins[parent] += 1
            neighbours = find_neighbours(pos[0], pos[1], dim)
            for point in neighbours:
                if not processed[point]:
                    processed[point] = True
                    if heights[point] != 9:
                        to_add[point] = parent

        to_process = to_add

    basins = [(k, v) for k, v in basins.items()]
    basins = sorted(basins, key = lambda x: x[1], reverse = True)

    print(f"Part two: {basins[0][1] * basins[1][1] * basins[2][1]}")

if __name__ == "__main__":
    heights, dim = read_heights()
    low_points = risk_levels(heights, dim)
    find_basins(heights, dim, low_points)
    
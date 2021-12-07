def read_positions():
    file_name = "Data/day7.txt"
    file = open(file_name, "r")

    for line in file:
        return sorted(list(map(int, line.split(","))))

def least_fuel(positions):
    median = positions[len(positions)//2]
    mean = sum(positions)//len(positions)

    fuel = sum(abs(x - median) for x in positions)
    print(f"Part one: {fuel}")

    fuel = min(sum(abs(x - mean) * (abs(x - mean) + 1)//2 for x in positions),
               sum(abs(x - mean - 1) * (abs(x - mean - 1) + 1)//2 for x in positions))
    print(f"Part two: {fuel}")

if __name__ == "__main__":
    positions = read_positions()
    least_fuel(positions)

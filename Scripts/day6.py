from collections import Counter

def read_fish():
    file_name = "Data/day6.txt"
    file = open(file_name, "r")
    
    for line in file:
        return list(map(int, line.split(",")))
    
def simulate_fish(fish, days):
    fish = Counter(fish)
    
    for t in range(days):
        new_fish = {}
        for i in range(1,9):
            new_fish[i-1] = fish.get(i, 0)
            
        new_fish[6] = new_fish.get(6, 0) + fish.get(0, 0)
        new_fish[8] = new_fish.get(8, 0) + fish.get(0, 0)
        fish = new_fish
            
    return sum(fish.values())
        
if __name__ == "__main__":
    fish = read_fish()
    print(f"Part one: {simulate_fish(fish, 80)}")
    print(f"Part two: {simulate_fish(fish, 256)}")
    
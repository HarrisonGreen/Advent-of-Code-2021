def read_depths():
    file_name = "Data/day1.txt"
    file = open(file_name, "r")
    depths = []
    
    for line in file:
        depths.append(int(line.strip("\n")))
        
    return depths

def depth_increases(depths):
    increases = [depths[i+1]-depths[i] > 0 for i in range(len(depths)-1)]
    print(f"Part one: {sum(increases)}")
    
def rolling_depth_increases(depths):
    rolling_depths = [sum(depths[i:i+3]) for i in range(len(depths)-2)]
    increases = [rolling_depths[i+1]-rolling_depths[i] > 0 for i in range(len(rolling_depths)-1)]
    print(f"Part two: {sum(increases)}")
        
if __name__ == "__main__":
    depths = read_depths()
    depth_increases(depths)
    rolling_depth_increases(depths)
    
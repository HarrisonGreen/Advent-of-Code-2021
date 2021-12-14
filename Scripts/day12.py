def read_tunnels():
    file_name = "Data/day12.txt"
    file = open(file_name, "r")
    tunnels = {}
    
    for line in file:
        line = line.strip("\n").split("-")
        tunnels[line[0]] = tunnels.get(line[0], set())
        tunnels[line[0]].add(line[1])
        tunnels[line[1]] = tunnels.get(line[1], set())
        tunnels[line[1]].add(line[0])
        
    return tunnels

def count_paths(tunnels):
    to_process = [["start"]]
    count = 0
    
    while to_process:
        path = to_process.pop(0)
        
        for cave in tunnels[path[-1]]:
            if cave == "end":
                count += 1
            elif ord(cave[0]) <= 90:
                to_process.append(path + [cave])
            elif cave not in path:
                to_process.append(path + [cave])
                
    print(f"Part one: {count}")
    
def count_relaxed_paths(tunnels):
    to_process = [(["start"], False)]
    count = 0
    
    while to_process:
        path, small_repeat = to_process.pop(0)
        
        for cave in tunnels[path[-1]]:
            if cave == "end":
                count += 1
            elif cave == "start":
                continue
            elif ord(cave[0]) <= 90:
                to_process.append((path + [cave], small_repeat))
            elif cave not in path:
                to_process.append((path + [cave], small_repeat))
            elif not small_repeat:
                to_process.append((path + [cave], True))
                
    print(f"Part two: {count}")
       
if __name__ == "__main__":
    tunnels = read_tunnels()
    count_paths(tunnels)
    count_relaxed_paths(tunnels)
    
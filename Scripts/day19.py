def read_scanners():
    file_name = "Data/day19.txt"
    file = open(file_name, "r")
    scanners = {}
    
    for line in file:
        if line.startswith("---"):
            n = int(line.strip(" ---\n")[8:])
            scanners[n] = []
        elif len(line) > 1:
            line = tuple(map(int, line.strip("\n").split(",")))
            scanners[n].append(line)
            
    return scanners

def rotate_beacons(beacons):
    rotations = []
    
    rotations.append([(x, y, z) for x, y, z in beacons])
    rotations.append([(-x, -y, z) for x, y, z in beacons])
    rotations.append([(-x, y, -z) for x, y, z in beacons])
    rotations.append([(x, -y, -z) for x, y, z in beacons])
    
    rotations.append([(-x, z, y) for x, y, z in beacons])
    rotations.append([(x, -z, y) for x, y, z in beacons])
    rotations.append([(x, z, -y) for x, y, z in beacons])
    rotations.append([(-x, -z, -y) for x, y, z in beacons])
    
    rotations.append([(-y, x, z) for x, y, z in beacons])
    rotations.append([(y, -x, z) for x, y, z in beacons])
    rotations.append([(y, x, -z) for x, y, z in beacons])
    rotations.append([(-y, -x, -z) for x, y, z in beacons])
    
    rotations.append([(y, z, x) for x, y, z in beacons])
    rotations.append([(-y, -z, x) for x, y, z in beacons])
    rotations.append([(-y, z, -x) for x, y, z in beacons])
    rotations.append([(y, -z, -x) for x, y, z in beacons])
    
    rotations.append([(z, x, y) for x, y, z in beacons])
    rotations.append([(-z, -x, y) for x, y, z in beacons])
    rotations.append([(-z, x, -y) for x, y, z in beacons])
    rotations.append([(z, -x, -y) for x, y, z in beacons])
    
    rotations.append([(-z, y, x) for x, y, z in beacons])
    rotations.append([(z, -y, x) for x, y, z in beacons])
    rotations.append([(z, y, -x) for x, y, z in beacons])
    rotations.append([(-z, -y, -x) for x, y, z in beacons])
    
    return rotations

def count_beacons(scanners):
    change = True
    positions = {pos: {} for pos in scanners.keys()}
    
    while change:
        change = False
        
        for i, a in enumerate(list(scanners.keys())[1:]):
            for b in list(scanners.keys())[i + 2:]:
                match, beacons, positions = find_common_beacons(scanners, a, b, positions)
                
                if match:
                    scanners[a] = beacons
                    del scanners[b]
                    change = True
                    break
            
            if change:
                break
            
    change = True
    while change:
        change = False
        
        for b in list(scanners.keys())[1:]:
            match, beacons, positions = find_common_beacons(scanners, 0, b, positions)
            
            if match:
                scanners[0] = beacons
                del scanners[b]
                change = True
                break
            
    print(f"Part one: {len(scanners[0])}")
        
    dist = 0
    for a_pos in positions[0].values():
        dist = max(dist, abs(a_pos[0]) + abs(a_pos[1]) + abs(a_pos[2]))
        for b_pos in positions[0].values():
            dist = max(dist, abs(a_pos[0] - b_pos[0]) +
                       abs(a_pos[1] - b_pos[1]) + abs(a_pos[2] - b_pos[2]))
            
    print(f"Part two: {dist}")

def find_common_beacons(scanners, a, b, positions):
    a_beacons = scanners[a]
    b_rotations = rotate_beacons(scanners[b])
    
    for a_pos in a_beacons:
        a_deltas = [(beacon[0] - a_pos[0],
                     beacon[1] - a_pos[1],
                     beacon[2] - a_pos[2]) for beacon in a_beacons]
    
        for rot, b_beacons in enumerate(b_rotations):
            for b_pos in b_beacons:
                b_deltas = [(beacon[0] - b_pos[0],
                             beacon[1] - b_pos[1],
                             beacon[2] - b_pos[2]) for beacon in b_beacons]
                
                if len(set(a_deltas).intersection(set(b_deltas))) >= 12:
                    adj_b_beacons = [(beacon[0] + a_pos[ 0],
                                      beacon[1] + a_pos[1],
                                      beacon[2] + a_pos[2]) for beacon in b_deltas]
                    positions[a][b] = (a_pos[0] - b_pos[0],
                                       a_pos[1] - b_pos[1],
                                       a_pos[2] - b_pos[2])
                    
                    for beacon, location in positions[b].items():
                        location = rotate_beacons([location])[rot][0]
                        positions[a][beacon] = (location[0] + positions[a][b][0],
                                                location[1] + positions[a][b][1],
                                                location[2] + positions[a][b][2])
                        
                    return True, set(a_beacons).union(set(adj_b_beacons)), positions
    
    return False, 0, positions
        
if __name__ == "__main__":
    scanners = read_scanners()
    count_beacons(scanners)
    
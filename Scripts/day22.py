import numpy as np

def read_steps():
    file_name = "Data/day22.txt"
    file = open(file_name,"r")
    steps = []
    
    for line in file:
        line = line.split()
        line[1] = line[1].split(",")
        for i in range(3):
            line[1][i] = line[1][i].split(".")
            
        line = [line[0], int(line[1][0][0][2:]), int(line[1][0][2]),
                int(line[1][1][0][2:]), int(line[1][1][2]),
                int(line[1][2][0][2:]), int(line[1][2][2])]
        steps.append(line)
        
    return steps

def initialise_reactor(steps):
    reactor = np.zeros([101, 101, 101], dtype=int)
    
    for step in steps:
        
        if max(abs(x) for x in step[1:]) > 50:
            continue
        
        if step[0] == "on":
            reactor[step[1]+50:step[2]+51, step[3]+50:step[4]+51, step[5]+50:step[6]+51] = 1
        else:
            reactor[step[1]+50:step[2]+51, step[3]+50:step[4]+51, step[5]+50:step[6]+51] = 0
            
    print(f"Part one: {sum(sum(sum(reactor)))}")
    
def reboot_reactor(steps):
    xx = set()
    yy = set()
    zz = set()
    
    for step in steps:
        xx.add(step[1])
        xx.add(step[2] + 1)
        yy.add(step[3])
        yy.add(step[4] + 1)
        zz.add(step[5])
        zz.add(step[6] + 1)
        
    xx = sorted(list(xx))
    yy = sorted(list(yy))
    zz = sorted(list(zz))
                
    reactor = set()
                
    for step in steps:
        
        x_vals = [x for x in xx if step[1] <= x <= step[2]]
        y_vals = [y for y in yy if step[3] <= y <= step[4]]
        z_vals = [z for z in zz if step[5] <= z <= step[6]]
        
        for x in x_vals:
            for y in y_vals:
                for z in z_vals:
                    if step[0] == "on":
                        reactor.add((x, y, z))
                    else:
                        try:
                            reactor.remove((x, y, z))
                        except KeyError:
                            pass
                        
    x_lengths = {}
    y_lengths = {}
    z_lengths = {}
    
    for i in range(len(xx) - 1):
        x_lengths[xx[i]] = xx[i+1] - xx[i]
    for i in range(len(yy) - 1):
        y_lengths[yy[i]] = yy[i+1] - yy[i]
    for i in range(len(zz) - 1):
        z_lengths[zz[i]] = zz[i+1] - zz[i]
                        
    total = 0
    for cube in reactor:
        total += x_lengths[cube[0]] * y_lengths[cube[1]] * z_lengths[cube[2]]
        
    print(f"Part two: {total}")
        
if __name__ == "__main__":
    steps = read_steps()
    initialise_reactor(steps)
    reboot_reactor(steps)
    
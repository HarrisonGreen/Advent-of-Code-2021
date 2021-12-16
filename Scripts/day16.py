from copy import copy
from math import prod

def read_transmission():
    file_name = "Data/day16.txt"
    file = open(file_name, "r")
    
    for line in file:
        return line
    
def convert_to_binary(transmission):
    output = ""
    
    for char in transmission:
        s = bin(int(char, 16))[2:]
        for i in range(4 - len(s)):
            s = "0" + s
        output += s
        
    return output

def parse_transmission(transmission):
    packets = []
    pos = 0
    
    while "1" in transmission[pos:]:
        s = copy(pos)
        v = int(transmission[pos:pos + 3], base = 2)
        t = int(transmission[pos + 3:pos + 6], base = 2)
        pos += 6
        
        if t == 4:
            n = transmission[pos + 1:pos + 5]
            while transmission[pos] == "1":
                pos += 5
                n += transmission[pos + 1:pos + 5]
            n = int(n, base = 2)
            pos += 5
            packets.append((s, v, t, n))
        else:
            a = int(transmission[pos], base = 2)
            if a == 0:
                b = int(transmission[pos + 1:pos + 16], base = 2) + pos + 15
                pos += 16
            else:
                b = int(transmission[pos + 1:pos + 12], base = 2)
                pos += 12
            packets.append((s, v, t, a, b))
            
    print(f"Part one: {sum(p[1] for p in packets)}")
    return packets

def nest_packets(packets):
    pos = len(packets)
    
    while pos > 0:
        pos -= 1
        
        if packets[pos][2] == 4:
            continue
        
        elif packets[pos][3] == 1:
            packets = packets[:pos] + [{packets[pos]: packets[pos + 1:pos + 1 + packets[pos][4]]}] + packets[pos + 1 + packets[pos][4]:]
            
        else:
            i = copy(pos)
            while True:
                i += 1
                
                if i >= len(packets):
                    packets = packets[:pos] + [{packets[pos]: packets[pos + 1:]}]
                    break
                
                if get_position(packets[i]) >= packets[pos][4]:
                    packets = packets[:pos] + [{packets[pos]: packets[pos + 1:i]}] + packets[i:]
                    break
                
    return packets[0]
        
def get_position(item):
    if type(item) == tuple:
        return item[0]
    else:
        return get_position(list(item.values())[0][0])
    
def eval_packet(packet):
    if type(packet) == tuple:
        return packet[3]
    
    operator = list(packet.keys())[0]
    sub_packets = list(packet.values())[0]
    
    if operator[2] == 0:
        return sum(eval_packet(sub) for sub in sub_packets)
    
    elif operator[2] == 1:
        return prod(eval_packet(sub) for sub in sub_packets)
    
    elif operator[2] == 2:
        return min(eval_packet(sub) for sub in sub_packets)
    
    elif operator[2] == 3:
        return max(eval_packet(sub) for sub in sub_packets)
    
    elif operator[2] == 5:
        if eval_packet(sub_packets[0]) > eval_packet(sub_packets[1]):
            return 1
        return 0
        
    elif operator[2] == 6:
        if eval_packet(sub_packets[0]) < eval_packet(sub_packets[1]):
            return 1
        return 0
        
    elif operator[2] == 7:
        if eval_packet(sub_packets[0]) == eval_packet(sub_packets[1]):
            return 1
        return 0
        
if __name__ == "__main__":
    transmission = read_transmission()
    transmission = convert_to_binary(transmission)
    packets = parse_transmission(transmission)
    packets = nest_packets(packets)
    print(f"Part two: {eval_packet(packets)}")
    
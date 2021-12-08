from collections import Counter

def read_signals():
    file_name = "Data/day8.txt"
    file = open(file_name, "r")
    signals = []
    digits = []
    
    for line in file:
        line = line.strip("\n").split(" | ")
        signals.append(line[0].split())
        digits.append(line[1].split())
        
    return signals, digits

def sort_connections(signals, digits):
    output = []
    
    for signal, numbers in zip(signals, digits):        
        connections = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
        letters = {i: set(connections.keys()) for i in range(2,8)}
        
        for segments in signal:
            letters[len(segments)] = letters[len(segments)].intersection(set(segments))
            
        connections["a"] = list(letters[3] - letters[2])[0]
        connections["f"] = list(letters[6].intersection(letters[2]))[0]
        connections["c"] = list(letters[2] - {connections["f"]})[0]
        connections["d"] = list(letters[4].intersection(letters[5]))[0]
        connections["b"] = list(letters[4].intersection(letters[6]) - {connections["f"]})[0]
        connections["g"] = list(letters[5].intersection(letters[6]) - {connections["a"]})[0]
        connections["e"] = list(set(connections.keys()) - {connections["a"]}
                                - {connections["b"]} - {connections["c"]} - {connections["d"]}
                                - {connections["f"]} - {connections["g"]})[0]
        
        connections = {v: k for k, v in connections.items()}
        
        for number in numbers:
            number = set(connections[letter] for letter in number)
            
            if number == {"c", "f"}:
                output.append(1)
            elif number == {"a", "c", "f"}:
                output.append(7)
            elif number == {"b", "d", "c", "f"}:
                output.append(4)
            elif number == {"a", "c", "d", "e", "g"}:
                output.append(2)
            elif number == {"a", "c", "d", "f", "g"}:
                output.append(3)
            elif number == {"a", "b", "d", "f", "g"}:
                output.append(5)
            elif number == {"a", "b", "c", "e", "f", "g"}:
                output.append(0)
            elif number == {"a", "b", "d", "e", "f", "g"}:
                output.append(6)
            elif number == {"a", "b", "c", "d", "f", "g"}:
                output.append(9)
            elif number == {"a", "b", "c", "d", "e", "f", "g"}:
                output.append(8)
                
    count = Counter(output)
    print(f"Part one: {count[1] + count[4] + count[7] + count[8]}")
    
    total = sum(output[i] * 10**(3 - (i%4)) for i in range(len(output)))
    print(f"Part two: {total}")
        
if __name__ == "__main__":
    signals, digits = read_signals()
    sort_connections(signals, digits)
    
def read_pairs():
    file_name = "Data/day14.txt"
    file = open(file_name, "r")
    pairs = {}
    
    for line in file:
        line = line.strip("\n").split(" -> ")
        pairs[(line[0][0], line[0][1])] = line[1]
        
    return pairs, set(pairs.values())

def insertion_process(template, pairs, letters, steps):
    pair_counts = {pair: 0 for pair in pairs.keys()}
    
    for i in range(len(template) - 1):
        pair_counts[(template[i], template[i + 1])] += 1
    
    for t in range(steps):
        new_pair_counts = {pair: 0 for pair in pairs.keys()}
        
        for pair, letter in pairs.items():
            new_pair_counts[(pair[0], letter)] += pair_counts[pair]
            new_pair_counts[(letter, pair[1])] += pair_counts[pair]
            
        pair_counts = new_pair_counts
        
    count = {letter: 0 for letter in letters}
    
    for pair, n in pair_counts.items():
        count[pair[0]] += n/2
        count[pair[1]] += n/2
        
    count[template[0]] += 0.5
    count[template[-1]] += 0.5
    
    return int(max(count.values()) - min(count.values()))
        
if __name__ == "__main__":
    template = "KBKPHKHHNBCVCHPSPNHF"
    pairs, letters = read_pairs()
    print(f"Part one: {insertion_process(template, pairs, letters, 10)}")
    print(f"Part two: {insertion_process(template, pairs, letters, 40)}")
    
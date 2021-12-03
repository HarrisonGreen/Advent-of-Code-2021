from copy import copy

def read_report():
    file_name = "Data/day3.txt"
    file = open(file_name, "r")
    report = []
    
    for line in file:
        report.append(line.strip("\n"))
        
    return report

def power_consumption(report):
    l = len(report[0])
    n = len(report)
    gamma = [0 for _ in range(l)]
    
    for i in range(n):
        for j in range(l):
            gamma[j] += int(report[i][j])
            
    for j in range(l):
        gamma[j] /= n
        gamma[j] = round(gamma[j] + 0.00001)
        
    gamma = "".join(list(map(str, gamma)))
    
    s = 0
    while gamma[s] == "0":
        s += 1
    gamma = gamma[s:]
    
    gamma = int(gamma, 2)
    epsilon = 2**l - 1 - gamma
    
    print(f"Part one: {gamma*epsilon}")
    
def life_support(report):
    oxygen = copy(report)
    pos = 0
    
    while len(oxygen) > 1:
        n = len(oxygen)
        
        value = sum(int(oxygen[i][pos]) for i in range(n))/n
        value = round(value + 0.00001)
        
        to_remove = []
        for rating in oxygen:
            if rating[pos] != str(value):
                to_remove.append(rating)
        for rating in to_remove:
            oxygen.remove(rating)
            
        pos += 1
        
    carbon = copy(report)
    pos = 0
    
    while len(carbon) > 1:
        n = len(carbon)
        
        value = sum(int(carbon[i][pos]) for i in range(n))/n
        value = 1 - round(value + 0.00001)
        
        to_remove = []
        for rating in carbon:
            if rating[pos] != str(value):
                to_remove.append(rating)
        for rating in to_remove:
            carbon.remove(rating)
            
        pos += 1
        
    s = 0
    while oxygen[0][s] == "0":
        s += 1
    oxygen = int(oxygen[0][s:], 2)
    
    s = 0
    while carbon[0][s] == "0":
        s += 1
    carbon = int(carbon[0][s:], 2)
        
    print(f"Part two: {oxygen*carbon}")
    
if __name__ == "__main__":
    report = read_report()
    power_consumption(report)
    life_support(report)
    
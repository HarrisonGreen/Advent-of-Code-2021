def read_lines():
    file_name = "Data/day10.txt"
    file = open(file_name, "r")
    lines = []
    
    for line in file:
        lines.append(line.strip("\n"))
        
    return lines

def score_lines(lines):
    syntax_score = 0
    autocomplete_scores = []
    
    for line in lines:
        passed, output = check_line(line)
        if not passed:
            syntax_score += output
        else:
            autocomplete_scores.append(completion_score(output))
            
    print(f"Part one: {syntax_score}")
    print(f"Part two: {sorted(autocomplete_scores)[len(autocomplete_scores)//2]}")

def check_line(line):
    
    while line:
        for i in range(len(line)):
            if line[i] in (")", "]", "}", ">"):
                break
            if i == len(line)-1:
                return True, line
                
        if line[i] == ")":
            score = 3
        elif line[i] == "]":
            score = 57
        elif line[i] == "}":
            score = 1197
        elif line[i] == ">":
            score = 25137
                
        if line[i-1] == "(" and line[i] != ")":
            return False, score
        elif line[i-1] == "[" and line[i] != "]":
            return False, score
        elif line[i-1] == "{" and line[i] != "}":
            return False, score
        elif line[i-1] == "<" and line[i] != ">":
            return False, score
        
        line = line[:i-1] + line[i+1:]
        
def completion_score(string):
    score = 0
    for char in reversed(string):
        score *= 5
        if char == "(":
            score += 1
        elif char == "[":
            score += 2
        elif char == "{":
            score += 3
        elif char == "<":
            score += 4
    return score

if __name__ == "__main__":
    lines = read_lines()
    score_lines(lines)
    
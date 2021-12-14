import matplotlib.pyplot as plt
import numpy as np

def read_instructions():
    file_name = "Data/day13_dots.txt"
    file = open(file_name, "r")
    dots = set()
    
    for line in file:
        line = line.strip("\n").split(",")
        dots.add(tuple(map(int, line)))
        
    file_name = "Data/day13_folds.txt"
    file = open(file_name, "r")
    folds = []
    
    for line in file:
        line = line.split()[-1].split("=")
        folds.append((line[0], int(line[1])))
        
    return dots, folds

def fold_paper(dots, folds):
    
    for i, fold in enumerate(folds):
        new_dots = set()
        
        if fold[0] == "x":
            for dot in dots:
                if dot[0] > fold[1]:
                    new_dots.add((2*fold[1] - dot[0], dot[1]))
                else:
                    new_dots.add((dot[0], dot[1]))
                    
        else:
            for dot in dots:
                if dot[1] > fold[1]:
                    new_dots.add((dot[0], 2*fold[1] - dot[1]))
                else:
                    new_dots.add((dot[0], dot[1]))
                    
        dots = new_dots
        if i == 0:
            print(f"Part one: {len(dots)}")
            
    return dots

def draw_dots(dots):
    x_max = sorted(dots, key = lambda x: x[0], reverse = True)[0][0]
    y_max = sorted(dots, key = lambda x: x[1], reverse = True)[0][1]
    
    grid = np.zeros([y_max + 1, x_max + 1])
    for dot in dots:
        grid[dot[1], dot[0]] = 1
        
    plt.imshow(grid)
    plt.show()
        
if __name__ == "__main__":
    dots, folds = read_instructions()
    dots = fold_paper(dots, folds)
    draw_dots(dots)
    
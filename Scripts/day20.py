import numpy as np

def read_image(n):
    file_name = "Data/day20.txt"
    file = open(file_name, "r")
    
    for i, line in enumerate(file):
        
        if i == 0:
            line = line.strip("\n")
            algorithm = []
            for char in line:
                if char == "#":
                    algorithm.append(1)
                else:
                    algorithm.append(0)
                    
        if i == 2:
            image = np.zeros([len(line) + 2*n - 1, len(line) + 2*n - 1], dtype = int)
            
        if i >= 2:
            line = line.strip("\n")
            for j, char in enumerate(line):
                if char == "#":
                    image[i + n - 2, j + n] = 1
                    
    return algorithm, image, len(line) + 2*n

def enhance_image(algorithm, image, dim, margin):
    new_image = np.zeros([dim, dim], dtype = int)
    
    if image[0][0] == 1:
        outer = algorithm[511]
    else:
        outer = algorithm[0]
        
    for i in range(dim):
        for j in range(dim):
            
            if i < margin or i > dim - margin - 1:
                new_image[i, j] = outer
                
            elif j < margin or j > dim - margin - 1:
                new_image[i, j] = outer
                
            else:
                index = list(image[i - 1:i + 2, j - 1:j + 2].flatten())
                index = "".join(str(x) for x in index)
                index = int(index, base = 2)
                new_image[i, j] = algorithm[index]
                
    return new_image

def enhance_n_times(algorithm, image, dim, n):
    
    for i in range(n):
        image = enhance_image(algorithm, image, dim, n - i)
        
    return sum(sum(image))

if __name__ == "__main__":
    n = 2
    algorithm, image, dim = read_image(n + 1)
    print(f"Part one: {enhance_n_times(algorithm, image, dim, n)}")
    
    n = 50
    algorithm, image, dim = read_image(n + 1)
    print(f"Part two: {enhance_n_times(algorithm, image, dim, n)}")
    
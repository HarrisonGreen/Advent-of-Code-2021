import numpy as np
from math import floor, ceil

def max_height(y_min):
    print(f"Part one: {(y_min * (y_min + 1))//2}")

def count_velocities(x_min, x_max, y_min, y_max):
    a_min = ceil(0.5 * np.sqrt(8 * x_min + 1) - 0.5)
    a_max = x_max
    b_min = y_min
    b_max = -y_min - 1
    count = 0
    
    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            
            t_min = ceil(b + 0.5 + 0.5 * np.sqrt((2 * b + 1)**2 - 8 * y_max))
            t_max = floor(b + 0.5 + 0.5 * np.sqrt((2 * b + 1)**2 - 8 * y_min))
            
            for t in range(t_min, t_max + 1):
                if t > a:
                    x = (a * (a + 1))//2
                else:
                    x = a * t - (t * (t - 1))//2
                    
                if x_min <= x <= x_max:
                    count += 1
                    break
                
                if x > x_max:
                    break
                
    print(f"Part two: {count}")

if __name__ == "__main__":
    x_min = 169
    x_max = 206
    y_min = -108
    y_max = -68
    max_height(y_min)
    count_velocities(x_min, x_max, y_min, y_max)
    
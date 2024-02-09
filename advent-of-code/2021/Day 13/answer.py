from utils import *
import numpy as np

def print_paper(dots):

    length = max([x[0] for x in dots]) + 1
    height = max([x[1] for x in dots]) + 1
    grid = [[0 for x in range(length)] for y in range(height)]

    for dot in dots:
        grid[dot[1]][dot[0]] = 1

    for h in range(height):
        row = ""
        for l in range(length):
            if grid[h][l]:
                row += "#"
            else:
                row += " "
        print(row)

if __name__ == "__main__":

    data = read_input("input.txt")
    dots = []
    folds = []

    done = False
    for line in data:
        if line == '\n':
            done = True
            continue

        if done:
            l = line.split(" ")
            folds.append(l[2].strip())
        else:
            temp = line.strip().split(",")
            dots.append((int(temp[0]), int(temp[1])))

    for fold in folds:
        temp = fold.split('=')
        partition = int(temp[1])
        way = 0 if temp[0] == "x" else 1

        for i, dot in enumerate(dots):
            
            if dot[way] > partition:
                distance = dot[way] - partition
                if way == 0:
                    dots[i] = (partition - distance, dot[1])
                else:
                    dots[i] = (dot[0], partition - distance)
        dots = list(set(dots))
        print(len(dots))

    print_paper(dots)
                
        
            

    
 
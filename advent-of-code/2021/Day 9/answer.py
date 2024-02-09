from utils import *
import numpy

def part_one(grid: List):
    
    riskfactor = 0
    basins = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            try:
                if grid[row][col] >= grid[row - 1][col]:
                    continue
            except IndexError:
                pass
            try:
                if grid[row][col] >= grid[row + 1][col]:
                    continue
            except IndexError:
                pass
            try:
                if grid[row][col] >= grid[row][col + 1]:
                    continue
            except IndexError:
                pass
            try:
                if grid[row][col] >= grid[row][col - 1]:
                    continue
            except IndexError:
                pass
            
            riskfactor += grid[row][col] + 1
            basins.append(grid[row][col])
            #print(f"New lowpoint found at: {row + 1}, {col + 1} - value of {riskfactor}")

    print(basins)
    return basins


def part_two(data: List):
    pass

if __name__ == '__main__':

    data = read_input("input.txt")
    grid = []
    for line in data:
        line = line.strip()
        row = [int(x) for x in line]
        grid.append(row)

    #Part 1:

    basins = part_one(grid)
    inp = open("input.txt").read().splitlines()
    out = 0
    rows = len(inp)
    cols = len(inp[0])

    basins2 = []
    for r in range(rows):
        for c in range(cols):
            q = inp[r][c]
            adj=[]
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    adj.append(inp[nr][nc])
            if all(i > q for i in adj):
                basins2.append(int(q))
                out += 1 + int(q)

    #Part 2:
    #print(part_two(data))


    



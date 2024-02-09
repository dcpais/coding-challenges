from utils import geometry
from utils.data import read_input
from utils.grid import neighbours

def check_flash(grid, has_flashed):
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > 9 and not has_flashed[i][j]:
                return True

    return False

def all_flash(grid):

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                return False

    return True

if __name__ == "__main__":
    data = read_input("input.txt")
    grid = []
    for line in data:   
        line = line.strip()
        row = []
        for num in line:
            row.append(int(num))
        grid.append(row)

    total_flashes = 0
    for step in range(300):
        grid = [[x + 1 for x in row] for row in grid]
        has_flashed = [[False for x in row] for row in grid]
        while check_flash(grid, has_flashed):
            for i, row in enumerate(grid):
                for j, fish in enumerate(row):
                    if fish > 9 and not has_flashed[i][j]:
                        grid[i][j] = 0
                        has_flashed[i][j] = True
                        total_flashes += 1
                        for n_r, n_c in neighbours((i, j), grid=grid):
                            if not has_flashed[n_r][n_c]:
                                grid[n_r][n_c] += 1
            
            #Part 2
            if all_flash(grid):
                for row in grid:
                    print(row)
                print(f"All flash at {step}")
                exit()

    
    print(total_flashes)
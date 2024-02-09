from utils import *
import random

def print_grid(grid, l, h):

    total = ""
    for y in range(h + 1):
        row = ""
        for x in range(l + 1):
            if (x, y) in grid.keys():
                c = grid[(x, y)]
            else:
                c = 0
            row += str(c) + " "

        row += "\n"
        total += row
    
    with open("output.txt", "w") as f:
        f.write(total)
    print(total)
            

# -------------- Define Helper Functions Here
def part_one(data):

    grid = {}
    
    #data = [("toggle", 0, 0, 999, 0)]
    for instruction in data:

        directive = instruction[0]
        x1, y1, x2, y2 = instruction[1:]

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                pos = (x, y)
                #print(pos)
                # Check if a light has been registered yet
                #if pos in grid.keys():
                #    continue
                #else:
                #    grid[pos] = 0 

                # Execute directive on current light
                if directive == "toggle":
                    #if grid[pos] == 1: 
                    #    grid[pos] = 0
                    #elif grid[pos] == 0: 
                    #    grid[pos] = 1
                    if pos in grid.keys():
                        grid.pop(pos)
                    else:
                        grid[pos] = 1
                
                elif directive == "off":
                    if pos in grid.keys():
                        grid.pop(pos)

                elif directive == "on":
                    grid[pos] = 1

    lightCount = 0
    print(len(grid))


def part_two(data):

    grid = {}

    for instruction in data:

        directive = instruction[0]
        x1, y1, x2, y2 = instruction[1:]

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                pos = (x, y)

                # Check if a light has been registered yet
                if pos in grid.keys():
                    pass
                else:
                    grid[pos] = 0 

                # Execute directive on current light
                if directive == "toggle":
                    grid[pos] += 2
                
                elif directive == "off":
                    grid[pos] = max(0, grid[pos] - 1)

                elif directive == "on":
                    grid[pos] += 1

    lightCount = 0
    for val in grid.values():
        lightCount += val
    return lightCount


# -------------- Main Entry Point
if __name__ == "__main__":
    data = read_input("input.txt")
    instructions = []
    for line in data:
        instruction = []
        for word in line.split(" "):
            
            if word in ["on", "off", "toggle"]:
                instruction.append(word)
            elif word in ["turn", "through"]:
                continue
            else:
                coords = word.split(",")
                instruction.append(int(coords[0]))
                instruction.append(int(coords[1]))

        instructions.append(tuple(instruction))

    #print(f"Total Lights turned on (p1): {part_one(instructions)}")
    print(f"Total Brightness of Lights (p2): {part_two(instructions)}")


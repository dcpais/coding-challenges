from utils import *

# -------------- Define Helper Functions Here


# -------------- Main Entry Point
if __name__ == "__main__":
    data = read_input("input.txt")[0]
    
    houses = {(0, 0): 2}
    pos1 = (0, 0)
    pos2 = (0, 0)
    toggle = True
    
    for d in data:
        if toggle:
            cpos = pos1
        else:
            cpos = pos2
        
        
        
        dx = cpos[0]
        dy = cpos[1]
        
        if d == "^":
            dy += 1
        elif d == ">":
            dx += 1
        elif d == "<":
            dx -= 1
        elif d == "v":
            dy -=  1
            
        pos = (dx, dy)
        if toggle:
            pos1 = pos
        else:
            pos2 = pos
        
        toggle = not toggle
        
        if pos in houses.keys():
            houses[pos] += 1
        else:
            houses[pos] = 1
        
    print(len(houses.keys()))    
        
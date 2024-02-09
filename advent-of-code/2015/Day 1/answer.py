from utils import *

# -------------- Define Helper Functions Here


# -------------- Main Entry Point
if __name__ == "__main__":
    data = read_input("input.txt")[0]
    level = 0
    idx = 0
    for direction in data:
        if direction == "(":
            level += 1
        elif direction == ")":
            level -= 1
        
        
        if level < 0:
            print(idx)
            break
        idx += 1
        
        print(level, idx)
        if level < 0:
            break
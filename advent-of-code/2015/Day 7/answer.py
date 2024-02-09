import numpy as np
from utils import *
import re

# -------------- Define Helper Functions Here
def part1(data):
    
    wires = {"b" : 16076}
    i = 0
    copy = data.copy()
    while len(copy) != 0:
        instruction = copy[i]
        s = instruction.strip().split(" ")
        output = s[-1]
        try:
            if len(s) == 3:
                if s[0].isalpha():
                    wires[output] = wires[s[0]]
                else:
                    wires[output] = int(s[0])


            elif len(s) == 4:
                if s[1].isalpha():
                    wires[output] = ~wires[s[1]]
                else:
                    wires[output] = ~int(s[1])
                    
            elif len(s) == 5:
                if s[0].isalpha(): in1 = wires[s[0]]
                else: in1 = int(s[0])    
                if s[2].isalpha(): in2 = wires[s[2]]
                else: in2 = int(s[2])

                output = s[4]
                
                if s[1] == "OR":
                    wires[output] = in1 | in2
                elif s[1] == "AND":
                    wires[output] = in1 & in2
                elif s[1] == "RSHIFT":
                    wires[output] = in1 >> in2
                elif s[1] == "LSHIFT":
                    wires[output] = in1 << in2  
                
            copy.pop(i)
            
        except KeyError:
            pass
        
        if len(copy) == 0:
            break
        i = (i + 1) % len(copy)
                
    fixed = np.array(list(wires.values()), dtype = np.uint16)
    return dict(zip(wires.keys(), fixed))    
    
    
def part2(data: list) -> dict:
    """
    Get answer for part 2
    """

    wires = {"b" : 16076}
    instructions = data.copy()
    while len(instructions) > 0:
        # Split our instruction and get our operation
        current = instructions.pop(0)
        inst = current.strip().split(" ")
        out = inst[-1]
        
        try:
            # Assignment
            if len(inst) == 3:
                wires[out] = getVal(inst[0], wires)

            # Apply NOT
            elif len(inst) == 4:
                wires[out] = ~getVal(inst[1], wires)

            # Apply other Operations
            else:
                # Get our inputs to the gate
                in1 = getVal(inst[0], wires)
                in2 = getVal(inst[2], wires)
                if inst[1] == "AND":
                    wires[out] = in1 & in2
                elif inst[1] == "OR":
                    wires[out] = in1 | in2
                elif inst[1] == "RSHIFT":
                    wires[out] = in1 >> in2
                elif inst[1] == "LSHIFT":
                    wires[out] = in1 << in2
        
        except KeyError:
            instructions.append(current)
    
    return wires

def getVal(node: str, wires: dict) -> int:
    if node.isalpha():
        return wires[node]
    else:
        return int(node)

# -------------- Main Entry Point
if __name__ == "__main__":
    data = read_input("input.txt")
    print(part2(data)["a"])
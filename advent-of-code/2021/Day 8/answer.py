from math import cos
from utils import *
import math


if __name__ == '__main__':
    data = read_input("input.txt")

    #filter data
    entries = []
    for entry in data:
        temp = entry.split(" | ")
        entries.append((temp[0], temp[1]))
    
    #something
    count = 0
    for entry in entries:
        for output in entry[1].strip().split(" "):
            if len(output) in [2, 4, 3, 7]:
                count += 1

    print(f"part 1: {count}")

    #Part 2 
    countTwo = 0
    for entry in entries:
        mappings = dict()
        lenfive = []
        lensix = []

        #Map NUMBER 1, 4, 7, 8
        for element in entry[0].split(" "):
            if len(element) == 2:
                mappings[1] = element
            elif len(element) == 3:
                mappings[7] = element
            elif len(element) == 4:
                mappings[4] = element
            elif len(element) == 7:
                mappings[8] = element
            elif len(element) == 5:
                lenfive.append(element)
            elif len(element) == 6:
                lensix.append(element)

        #Map NUMBER 6
        for number in lensix:
            for digit in mappings[1]:
                if digit not in number:
                    mappings[6] = number
                    lensix.pop(lensix.index(number))
                    break
    
        #Map NUMBER 3, 2 and 5
        for number in lenfive:
            if all(c in number for c in mappings[1]):
                mappings[3] = number
            else:
                if all(c in mappings[6] for c in number):
                    mappings[5] = number
                else:
                    mappings[2] = number

        #Map number 9 and 0
        #print(lensix)
        for number in lensix:
            if all(c in number for c in mappings[4]):
                mappings[9] = number    
            else:
                mappings[0] = number
            
        output = []
        print(mappings)
        for element in entry[1].strip().split(" "):
            
            for key, val in mappings.items():
                if len(element) == len(val):
                    if all(c in val for c in element):
                        output.append(key)
        #print(output)
        countTwo += int(''.join([str(x) for x in output]))
    print(countTwo)

                    

    



    



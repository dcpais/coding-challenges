import collections
from typing import Collection
from utils import *
import numpy as np
import collections

if __name__ == '__main__':
    data = read_input("input.txt")
    polymer = data[0].strip()
    data.pop(0); data.pop(0)
    rules = dict()
    pairs = dict()
    count = dict()

    for line in data:
        temp = line.split(" -> ")
        rules[temp[0]] = temp[1].strip()
        pairs[temp[0]] = 0

    for rule in rules.keys():
        for char in rule:
            count[char] = 0

    for i in range(len(polymer) - 1):
        pairs[polymer[i: i + 2]] += 1
        
    for i in range(len(polymer)):
        count[char] += 1

    for step in range(40):
        #print(f"Step {step + 1}")
        new_count = pairs.copy()
        for key in new_count.keys():
            new_count[key] = 0
        for pair, val in pairs.items():
            rule = rules[pair]
            key1 = pair[0] + rule
            key2 = rule + pair[1]
            new_count[key1] += val
            new_count[key2] += val
            count[rule] += val
        pairs = new_count
        
    print(count)
    #print(pairs)
    print(max(count.values()) - min(count.values()))



    
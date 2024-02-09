from math import cos
from utils import *
import math

def get_cumulative_sum(num):
    return (num * (num + 1)) / 2

if __name__ == '__main__':
    data = read_input("input.txt")
    data = [int(x) for x in data[0].split(",")]
    
    bestCost = math.inf
    for i in range(max(data)):
        currentCost = 0
        for crab in data:
            currentCost += get_cumulative_sum(abs(i - crab))
        
        if currentCost < bestCost:
            bestCost = currentCost

    print(int(bestCost))

    
        
    

    



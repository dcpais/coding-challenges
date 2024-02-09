from math import cos
from utils import *
import math


if __name__ == '__main__':
    data = read_input("input.txt")
    data = [int(x) for x in data]
    
    for i in data: 
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(i * j * k)
                    
                        
                    

    



    



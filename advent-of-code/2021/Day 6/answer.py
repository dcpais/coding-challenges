from typing import Optional
from utils import *

class LanternFish:

    def __init__(self, countdown: int):
        self._count = countdown

    def update(self):
        self._count -= 1
        if self._count < 0:
            self._count = 6
            return LanternFish(8)
        else:
            return None

    def __repr__(self):
        return f"{self._count}"

    def __str__(self):
        return f"{self._count}"


def step_one(data: List[int]): 
    fishes = []
    for fish in data:
        fishes.append(LanternFish(fish))

    #80 days
    for day in range(80):
        dayRep = f"After {day + 1} days: "
        toAdd = []
        for fish in fishes:
            spawned = fish.update()
            if spawned is not None:
                toAdd.append(spawned)
            dayRep += repr(fish) + " "
        fishes.extend(toAdd)
        #print(dayRep)
    
    print(len(fishes))


def step_two(data: List[int]):

    cycle = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in data:
        cycle[fish] += 1

    for day in range(256):
        spawnCount = cycle.pop(0)
        cycle[6] += spawnCount
        cycle.append(spawnCount)

    print(sum(cycle))
        


if __name__ == '__main__':
    data = read_input("input.txt")
    data = [int(x) for x in data[0].split(",")]
    
    #step_one(data)
    step_two(data)
        







from __future__ import annotations
from utils import *
import heapq

class Node(object):

    def __init__(self, path: List[Tuple[int, int]], cost: int):
        self._path = path
        self._cost = cost

    def at(self):
        return self._path[-1]

    def __eq__(self, __o: Node) -> bool:
        return self._path == __o._path

    def __lt__(self, __o: Node) -> bool:
        return self._cost < __o._cost

    def __gt__(self, __o: Node) -> bool:
        return self._cost > __o._cost

    #def __hash__(self):
    #    return hash(self._path) + hash(self._cost)

    def __repr__(self):
        return f"Path: {self._path} Cost: {self._cost}"


def ucs(grid: List[int]):
    
    frontier = [Node([(0, 0)], 0)]
    visited = dict()

    while frontier:
        current = heapq.heappop(frontier)
        if current.at()[0] == len(grid) - 1 and \
            current.at()[1] == len(grid) - 1:
            return current

        visited[current.at()] = current._cost
        for i, j in neighbours(current.at(), grid):
            cost = current._cost + grid[i][j]
            successor = Node(current._path + [(i, j)], cost)
        
            if (i, j) not in visited.keys() or cost < visited[(i, j)]:
                visited[(i, j)] = cost
                heapq.heappush(frontier, successor)

    return None


if __name__ == '__main__': 
    data = read_input("input.txt")
    data = int_lines_to_grid(data)
    
    #Part 1:
    #print(ucs(data))

    #Part 2:
    grid = []
    for row in data:
        new_row = []
        for i in range(5):
            for col in row:
                new_row.append((col + i - 1) % 9 + 1)
        grid.append(new_row)

    itt = grid.copy()
    for i in range(1, 5):
        for row in itt:
            new_row = []
            for col in row:
                new_row.append((col + i - 1) % 9 + 1)
            grid.append(new_row)

    path = ucs(grid)
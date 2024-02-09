import math
import heapq

n, s = [int(x) for x in input().strip().split(" ")]

cities = []
for i in range(n):
    cities.append([int(x) for x in input().strip().split(" ")])

# Construct graph
edges = dict([(i, []) for i in range(n)])
for i, (top, bot) in enumerate(cities[:-1]):
    for j, (top1, bot1) in enumerate(cities[i+1:], start = i + 1):
        if top == top1 or bot == bot1:
            edges[i].append(j)
            edges[j].append(i)

# BFS search, considering steps.
def doBFS(start, end, graph):

    frontier = [(start, 0)]
    visited = set()
    while frontier:
        current, step = frontier.pop(0)
        
        if current == end:
            return step
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                frontier.append((neighbour, step + 1))
                visited.add(neighbour)

    return -1

# Iterate over all queries and output the degree of connection
q = int(input())
friendlies = []
for i in range(q):
    start, end = [int(x) - 1 for x in input().strip().split(' ')]
    friendlies.append(doBFS(start, end, edges))

for friend in friendlies:
    print(friend)





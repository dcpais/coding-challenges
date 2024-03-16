class Solution:

    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        queue = []
        for x, y in points:
            heapq.heappush(queue, Point(x, y))

        print(queue)
        return [(a.x, a.y) for a in heapq.nsmallest(k, queue)]

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, o):
        return o.x == self.x and o.y == self.y

    def __lt__(self, o):
        return self.dist() < o.dist()

    def __gt__(self, o):
        return self.dist() > o.dist()
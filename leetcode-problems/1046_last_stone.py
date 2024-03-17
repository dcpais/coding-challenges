class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            print(x ,y)
            if x != y:
                heapq.heappush(heap, y - x)

        return 0 if len(heap) == 0 else heap[0]
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k - 1
        self.queue = sorted(nums)[::-1]

    def add(self, val: int) -> int:
        index = 0
        while index < len(self.queue) and val <= self.queue[index]:
            index += 1
        
        if index == len(self.queue):
            self.queue.append(val)
        else:
            self.queue.insert(index, val)
        
        return self.queue[self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
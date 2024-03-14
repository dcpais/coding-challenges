class Solution:
    def isHappy(self, n: int) -> bool:
        digits = str(n)
        visited = set()
        visited.add(digits)

        while digits != "1":
            digSum = sum(map(lambda x: int(x)**2, digits))
            if digSum in visited:
                return False
            visited.add(digSum)
            digits = str(digSum)

        return True
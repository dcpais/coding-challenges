class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i, current, total):
            if total == target:
                combinations.append(current)
                return
            elif total > target:
                return

            backtrack(i, current + [candidates[i]], total + candidates[i])
            if i < len(candidates) - 1:
                backtrack(i + 1, current, total)  

        backtrack(0, [], 0)
        return combinations          
            
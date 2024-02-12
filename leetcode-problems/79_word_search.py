class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])

        # Search algorithm
        def dfs(x, y, i, visited):
            # Prune search
            if board[x][y] != word[i]:
                return False

            # Found finish
            if i == len(word) - 1:
                return True

            visited.add((x, y))
            for dx, dy in directions:
                nx = dx + x
                ny = dy + y

                if not 0 <= nx < m or not 0 <= ny < n:
                    continue
                if (nx, ny) in visited:
                    continue

                nextChar = board[nx][ny]
                if nextChar == word[i + 1]:
                    if dfs(nx, ny, i + 1, visited):
                        return True
            visited.remove((x, y))
            return False

        # Run search on each tile
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, set()):
                    return True
        return False
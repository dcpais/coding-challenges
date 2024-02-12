class TrieNode:

    def __init__(self):
        self._children = dict()
        self._isEnd = False

class Trie:

    def __init__(self):
        self._head = TrieNode()

    def insert(self, word: str) -> None:
        current = self._head
        for i in range(len(word)):

            if not word[i] in current._children:
                current._children[word[i]] = TrieNode()
            current = current._children[word[i]]
            
        current._isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        allWords = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])

        # Construct Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Search with DFS
        def dfs(trieNode, boardNode, visited):
            x, y, word = boardNode

            if trieNode._isEnd:
                allWords.append(word)
            visited.add((x, y))

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nextChar = board[nx][ny]
                    if nextChar not in trieNode._children.keys():
                        continue
                    
                    if (nx, ny) not in visited:
                        dfs(trieNode._children[nextChar], [nx, ny, word + nextChar], visited)
                    
            visited.remove((x, y))

        # Search each Tile
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char not in trie._head._children.keys():
                    continue
                dfs(trie._head._children[char], [i, j, char], set())
        
        return list(set(allWords))
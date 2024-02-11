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

    def search(self, word: str) -> bool:
        current = self._head
        for i in range(len(word)):
            if not word[i] in current._children.keys():
                return False
            current = current._children[word[i]]
        
        return True if current._isEnd else False           

    def startsWith(self, word: str) -> bool:
        current = self._head
        for i in range(len(word)):
            if not word[i] in current._children.keys():
                return False
            current = current._children[word[i]]
        
        return True

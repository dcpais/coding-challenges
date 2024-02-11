class Node:

    def __init__(self):
        self._nexts = dict()
        self._isEnd = False

class WordDictionary:

    def __init__(self, head = None):
        if head != None: self._head = head
        else: self._head = Node()

    def addWord(self, word: str) -> None:
        current = self._head
        for i in range(len(word)):
            if not word[i] in current._nexts:
                current._nexts[word[i]] = Node()
            current = current._nexts[word[i]]

        current._isEnd = True    

    def search(self, word: str) -> bool:
        current = self._head 
        for i in range(len(word)):
            if word[i] == ".":
                for key, node in current._nexts.items():
                    toSearch = WordDictionary(node)
                    if toSearch.search(word[i + 1:]): return True
                return False
            elif word[i] not in current._nexts:
                return False
            current = current._nexts[word[i]]
        
        return True if current._isEnd else False
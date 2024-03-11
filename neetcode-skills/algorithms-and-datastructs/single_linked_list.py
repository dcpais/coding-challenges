class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.count = 0
    
    def get(self, index: int) -> int:
        current = self.head

        if not 0 <= index < self.count: return -1

        while index > 0 and current:
            current = current.next
            index -= 1
        
        return current.val

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        self.count += 1

    def insertTail(self, val: int) -> None:
        if not self.head: 
            self.head = Node(val)
            self.count += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(val)
        self.count += 1


    def remove(self, index: int) -> bool:
        if not self.head: return False
        if index == 0:
            self.head = self.head.next
            self.count -= 1
            return True
        if not 0 <= index < self.count:
            return False

        prev = None
        current = self.head

        while index > 0 and current:
            prev = current
            current = current.next
            index -= 1


        prev.next = current.next
        self.count -= 1
        return True
        

    def getValues(self) -> List[int]:
        vals = []
        current = self.head
        while current:
            vals.append(current.val)
            current = current.next
        return vals

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

        if self.size == 0:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next

            if self.size == 1:
                self.tail = None
            
            self.size -= 1
            return True
        
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        removed = prev.next
        prev.next = removed.next
        if removed == self.tail:
            self.tail = prev
        self.size -= 1
        return True 

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.data)
            curr = curr.next

        return values

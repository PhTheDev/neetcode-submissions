class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.front = self.back = node
        else:
            node.prev = self.back
            self.back.next = node
            self.back = node
        self.size += 1
        
    def appendleft(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.front = self.back = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        value = self.back.val
        if self.front == self.back:
            self.front = self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None
        self.size -= 1
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.front.val
        if self.front == self.back:
            self.front = self.back = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return value

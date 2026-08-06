class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.esq = None
        self.dir = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self._insert(self.root, key, val)

    def _insert(self, node, key: int, val: int):
        if node is None:
            return Node(key, val)
        if key > node.key:
            node.dir = self._insert(node.dir, key, val)
        elif key < node.key:
            node.esq = self._insert(node.esq, key, val)
        else:
            node.val = val
        return node

    def get(self, key: int) -> int:
        return self._get(self.root, key)
    
    def _get(self, node, key: int):
        if node is None:
            return -1
        if key == node.key:
            return node.val
        if key < node.key:
            return self._get(node.esq, key)
        else:
            return self._get(node.dir, key)

    def getMin(self) -> int:
        return self._getMin(self.root)

    def _getMin(self, node):
        if node is None:
            return -1
        elif not node.esq:
            return node.val
        else:
            return self._getMin(node.esq)

    def getMax(self) -> int:
        return self._getMax(self.root)

    def _getMax(self, node):
        if node is None:
            return -1
        elif not node.dir:
            return node.val
        else:
            return self._getMax(node.dir)

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.esq = self._remove(node.esq, key)
        elif key > node.key:
            node.dir = self._remove(node.dir, key)
        else:
            if node.esq is None:
                return node.dir
            elif node.dir is None:
                return node.esq
            else:
                successor = self._getMinNode(node.dir)
                node.key = successor.key
                node.val = successor.val
                node.dir = self._remove(node.dir, successor.key)

        return node

    def _getMinNode(self, node):
        while node.esq:
            node = node.esq
        return node

    def getInorderKeys(self) -> List[int]:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.esq, result)
        result.append(node.key)
        self._inorder(node.dir, result)
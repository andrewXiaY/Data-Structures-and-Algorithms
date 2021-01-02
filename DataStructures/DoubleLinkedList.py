# 这是双链表中的节点实现
from algorithms.DataStructures.Node import Node


class DLLNode(Node):
    def __init__(self, data=None, prv=None, nxt=None):
        super().__init__(data)
        self.prev = prv
        self.next = nxt


class DoubleLinkedList:
    def __init__(self):
        self.head = DLLNode()
        self.tail = DLLNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        self.all_nodes = set()
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        return self._get(index).data

    def __setitem__(self, key, value):
        node = self._get(key)
        node.data = value

    def __str__(self):
        res = []

        curr = self.head.next
        while curr != self.tail:
            res.append(curr.data)
            curr = curr.next

        return str(res)

    def _get(self, index):
        if not isinstance(index, int):
            raise Exception("Expect int, but got {}".format(type(index)))

        index = index if index >= 0 else self._size + index

        if index >= self._size or index < 0:
            raise Exception('Index out of range')

        curr = self.head.next
        while index > 0:
            curr = curr.next
            index -= 1

        return curr

    def _remove_node(self, node):
        if id(node) not in self.all_nodes:
            raise Exception("Try to remove a non-exist node")
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node: DLLNode):
        node.next = self.head.next
        self.head.next.prev = node

        node.prev = self.head
        self.head.next = node

        self.all_nodes.add(id(node))

    def _add_back(self, node: DLLNode):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node
        self.all_nodes.add(id(node))

    def append(self, data):
        node = DLLNode(data)
        self._add_back(node)
        self._size += 1

    def pop(self, index=0):
        node = self._get(index)
        self._remove_node(node)
        self._size -= 1
        return node.data

    def insert(self, index, node):
        index = index if index >= 0 else index + self._size

        if index >= self._size or index < 0:
            raise Exception("Index out of range")

        curr = self._get(index)
        curr.prev.next = node
        node.prev = curr.prev

        curr.prev = node
        node.next = curr


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(dll._size)
    dll.pop()
    print(dll._size)
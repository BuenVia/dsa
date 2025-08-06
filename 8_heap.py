class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index -1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        cur = len(self.heap) -1
        while cur > 0 and self.heap[cur] > self.heap[self._parent(cur)]:
            self._swap(cur, self._parent(cur))
            cur = self._parent(cur)

mh = MaxHeap()

mh.insert(99)
mh.insert(83)
mh.insert(71)
mh.insert(63)

print(mh.heap)

mh.insert(100)
print(mh.heap)

mh.insert(75)
print(mh.heap)
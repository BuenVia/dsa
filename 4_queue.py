class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node

    def traverse(self):
        cur = self.first
        ex = ""
        while cur:
            ex += f"{cur.value}-->"
            cur = cur.next
        print(ex[0:-3])

    def enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node

    def dequeue(self):
        temp = self.first
        self.first = self.first.next
        temp.next = None

qu = Queue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.dequeue()
qu.enqueue(4)
qu.dequeue()

qu.traverse()

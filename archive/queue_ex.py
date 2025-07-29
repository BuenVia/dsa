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
        example = ""
        while cur:
            example += f"{cur.value}--->"
            cur = cur.next
        print(f"[{example[0:-4]}]")

    def enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node
        
    def dequeue(self):
        temp = self.first
        self.first = self.first.next
        temp.next = None


print("Set queue with 1")
queue = Queue(1)
queue.traverse()
print("Enqueue 2")
queue.enqueue(2)
queue.traverse()
print("Enqueue 3")
queue.enqueue(3)
queue.traverse()
print("Dequeue 1")
queue.dequeue()
queue.traverse()
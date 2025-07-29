class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def traverse(self):
        cur = self.head
        ex = ""
        while cur:
            ex += f"{cur.value}-->"
            cur = cur.next
        print(ex[0:-3])

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert(self, index, value):
        new_node = Node(value)
        cur = self.head
        for _ in range(index -1):
            cur = cur.next
        before = cur
        after = cur.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def pop_first(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None

    def pop_middle(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        before = cur.prev
        after = cur.next
        before.next = after
        after.prev = before
        cur.prev = None
        cur.next = None

    def pop_last(self):
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None

dll = DoublyLinkedList(2)
dll.prepend(1)
dll.append(4)
dll.insert(2, 3)
dll.pop_first()
dll.pop_middle(1)
dll.pop_last()

dll.traverse()
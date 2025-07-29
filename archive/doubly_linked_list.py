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
        while cur:
            print(cur.value)
            cur = cur.next

    def prepend(self, value):
        new_node = Node(value)
        after = self.head
        self.head = new_node
        self.head.next = after
        after.prev = self.head

    def insert(self, index, value):
        new_node = Node(value)
        cur = self.head
        for _ in range(index -1):
            cur = cur.next
        before = cur
        after = cur.next
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = self.tail.next
        
    def pop_first(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_middle(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        before = cur.prev
        after = cur.next
        before.next = after
        after.prev = before

    def pop(self):
        before = self.tail.prev
        self.tail.prev = None
        self.tail = before
        self.tail.next = None

dll = DoublyLinkedList(2)
dll.prepend(1)
dll.append(3)
dll.pop()
dll.traverse()
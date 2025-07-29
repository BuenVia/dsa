class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
        self.head = new_node

    def insert(self, index, value):
        new_node = Node(value)
        cur = self.head
        for _ in range (index -1):
            cur = cur.next
        temp = cur.next
        cur.next = new_node
        new_node.next = temp

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def pop_first(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None

    def pop_middle(self, index):
        pre = None
        cur = self.head
        for _ in range(index):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        cur = None

    def pop_last(self):
        pre = None
        cur = self.head
        while cur.next != None:
            pre = cur
            cur = cur.next
        self.tail = pre
        self.tail.next = None

ll = LinkedList(2)
ll.prepend(1)
ll.prepend(0)
ll.append(5)
ll.insert(3, 4)
ll.insert(3, 3)
ll.pop_first()
ll.pop_middle(2)
ll.pop_last()
ll.pop_last()
ll.traverse()

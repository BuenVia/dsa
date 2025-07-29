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
        while cur:
            print(cur.value)
            cur = cur.next

    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        self.head = new_node
        self.head.next = temp

    def insert(self, index, value):
        new_node = Node(value)
        cur = self.head
        for _ in range(index -1):
            cur = cur.next
        temp = cur.next
        cur.next = new_node
        new_node.next = temp

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def pop_first(self):
        self.head = self.head.next

    def delete_middle(self, index):
        pre = None
        cur = self.head
        for _ in range(index):
            pre = cur
            cur = cur.next
        pre.next = cur.next

    def pop(self):
        pre = None
        cur = self.head
        while cur.next:
            pre = cur
            cur = cur.next
        self.tail = pre
        self.tail.next = None


ll = LinkedList(4)
ll.prepend(1)
ll.insert(1, 2)
ll.append(3)
# ll.pop_first()
# ll.delete_middle(1)
ll.pop()
ll.pop()
ll.traverse()
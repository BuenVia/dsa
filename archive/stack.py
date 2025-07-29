class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node

    def traverse(self):
        cur = self.top
        example = ""
        while cur:
            example += f"{cur.value}--->"
            # print(cur.value)
            cur = cur.next
        print(f"[{example[0:-4]}]")

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        temp = self.top
        self.top = self.top.next
        temp.next = None


print("Create Stack with 1")
stack = Stack(1)
stack.traverse()
print("Push 2")
stack.push(2)
stack.traverse()
print("Push 3")
stack.push(3)
stack.traverse()
print("Pop 3")
stack.pop()
stack.traverse()
print("Pop 2")
stack.pop()
stack.traverse()
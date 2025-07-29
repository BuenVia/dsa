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
        while cur:
            print(cur.value)
            cur = cur.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        temp = self.top
        self.top = self.top.next
        temp.next = None

st = Stack(1)
st.push(2)
st.push(3)
st.pop()
st.push(4)
st.pop()
st.push(5)

st.traverse()
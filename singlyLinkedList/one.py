

class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

n1 = Node(20) 
n2 = Node(30) 
n3 = Node(40)

n1.Next = n2
n2.Next = n3

l1 = singlyLinkedList()
l1.head = n1

current = l1.head

while(current):
    print(current.data)
    current = current.Next


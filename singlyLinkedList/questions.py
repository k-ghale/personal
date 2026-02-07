
# create a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        

# create a node
n1 = Node(10)
n2 = Node(10)
n3 = Node(10)
n4 = Node(10)

#assigning next
n1.next = n2
n2.next = n3
n3.next = n4

#create a singly linked list
l1 = SinglyLinkedList()
l1.head = n1

# traverse func
l1.traverse()
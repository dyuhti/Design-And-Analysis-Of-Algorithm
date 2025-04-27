class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return self.head

    def s(self):
        data = []
        current = self.head
        while current:
            data.append(current.data)
            current = current.next
        r = sorted(data)
        return r


l = LinkedList()
#l1
l.insert(1)
l.insert(2)
l.insert(4)
#l2
l.insert(1)
l.insert(3)
l.insert(4)

print(l.s())


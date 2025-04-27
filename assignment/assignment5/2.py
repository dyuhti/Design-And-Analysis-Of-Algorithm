class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self,data):
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
            data.extend(current.data)
            current = current.next
        r = sorted(data)
        return r


ar = [[1,4,5],[1,3,4],[2,6]]
l = Linked_list()
for i in range(len(ar)):
    l.insert(ar[i])

print(l.s())

































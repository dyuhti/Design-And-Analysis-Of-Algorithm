class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
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

    def dup(self):
        data = []
        current = self.head
        while current:
            data.append(current.data)
            current = current.next

        i = 0
        while i < len(data) - 1:
            if data[i] == data[i + 1]:
                data.pop(i)
            else:
                i += 1
        return data


ar = [1, 1, 2]
l = Linked_list()
for i in range(len(ar)):
    l.insert(ar[i])
print(l.dup())

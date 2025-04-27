from collections import deque

class Queue:
    def __init__(self, nums):
        self.queue = deque(nums)
        self.unique_elements = set(nums)

    def showUnique(self):
        if self.unique_elements:
            return self.queue[0]
        return -1

    def add(self, value):
        if value in self.unique_elements:
            self.unique_elements.remove(value)
        else:
            self.queue.append(value)
            self.unique_elements.add(value)

        while self.queue and self.queue[0] not in self.unique_elements:
            self.queue.popleft()

# Example usage
s = ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
ar = [[2, 3, 5], [], [5], [], [2], [], [3], []]

firstUnique = None
ans = []

for i, op in enumerate(s):
    if op == "FirstUnique":
        firstUnique = Queue(ar[i])
        ans.append(None)
    elif op == "showFirstUnique":
        ans.append(firstUnique.showUnique())
        ans.append(",null")
    elif op == "add":
        firstUnique.add(ar[i][0])

print(ans)
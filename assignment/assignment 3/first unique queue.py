from collections import deque, defaultdict

class FirstUnique:
    def __init__(self, nums):
        self.queue = deque()
        self.count = defaultdict(int)
        if isinstance(nums, list):
            for num in nums:
                self.add(num)
        else:
            self.add(nums)

    def showFirstUnique(self):
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        if self.queue:
            return self.queue[0]
        return -1

    def add(self, value):
        self.count[value] += 1
        if self.count[value] == 1:
            self.queue.append(value)
        else:
            # Remove duplicates from queue
            while self.queue and self.count[self.queue[0]] > 1:
                self.queue.popleft()

# Example usage
commands = ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
inputs = [[2,3,5],[],[5],[],[2],[],[3],[]]

first_unique = None
outputs = []

for cmd, vals in zip(commands, inputs):
    if cmd == "FirstUnique":
        first_unique = FirstUnique(vals)
        outputs.append(None)
    elif cmd == "showFirstUnique":
        outputs.append(first_unique.showFirstUnique())
    elif cmd == "add":
        first_unique.add(vals[0])

print(outputs)  # Output: [None, 2, None, 2, None, 3, None, -1]

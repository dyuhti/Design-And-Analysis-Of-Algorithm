class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def smallestStringWithSwaps(s, pairs):
    n = len(s)
    uf = UnionFind(n)

    # Union pairs
    for pair in pairs:
        uf.union(pair[0], pair[1])

    # Group indices
    groups = {}
    for i in range(n):
        root = uf.find(i)
        if root in groups:
            groups[root].append(i)
        else:
            groups[root] = [i]

    # Sort characters within each group
    sorted_groups = {}
    for root, indices in groups.items():
        chars = [s[idx] for idx in indices]
        sorted_chars = sorted(chars)
        sorted_groups[root] = sorted_chars

    # Construct lexicographically smallest string
    result = [''] * n
    for root, indices in groups.items():
        sorted_chars = sorted_groups[root]
        for i, idx in enumerate(indices):
            result[idx] = sorted_chars[i]

    return ''.join(result)


# Example usage
s = "dcab"
pairs = [[0, 3], [1, 2], [0, 2]]
print(smallestStringWithSwaps(s, pairs))  # Output: "bacd"

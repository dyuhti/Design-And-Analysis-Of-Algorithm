class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def find_closest_values(self, query):
        closest_smaller = self._find_largest_smaller_or_equal(query, self.root)
        closest_larger = self._find_smallest_larger_or_equal(query, self.root)

        if closest_smaller is not None:
            closest_smaller = closest_smaller.data
        if closest_larger is not None:
            closest_larger = closest_larger.data

        return [closest_smaller, closest_larger]

    def _find_largest_smaller_or_equal(self, query, node):
        if node is None:
            return None

        if query == node.data:
            return node

        if query < node.data:
            return self._find_largest_smaller_or_equal(query, node.left)

        right_subtree_result = self._find_largest_smaller_or_equal(query, node.right)
        if right_subtree_result is not None:
            return right_subtree_result

        return node

    def _find_smallest_larger_or_equal(self, query, node):
        if node is None:
            return None

        if query == node.data:
            return node

        if query > node.data:
            return self._find_smallest_larger_or_equal(query, node.right)

        left_subtree_result = self._find_smallest_larger_or_equal(query, node.left)
        if left_subtree_result is not None:
            return left_subtree_result

        return node


# Example usage:
n = BST()
root = [6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14]
queries = [2, 5, 16]

# Insert elements into the BST
for i in root:
    if i is not None:
        n.insert(i)

# Process each query
results = []
for query in queries:
    result = n.find_closest_values(query)
    results.append(result)

print("Output:", results)  # Expected output: [[2, 2], [4, 6], [15, None]]

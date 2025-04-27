class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data,node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def swap_nodes(self, level):
        if self.root is None:
            return

        queue = [self.root]
        current_level = 1
        nodes_to_swap = []

        while queue:
            size = len(queue)

            if current_level == level:
                for i in range(size):
                    node = queue.pop(0)
                    nodes_to_swap.append(node)
            else:
                for i in range(size):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if nodes_to_swap:
                for i in range(0, len(nodes_to_swap) - 1, 2):
                    nodes_to_swap[i].data, nodes_to_swap[i + 1].data = nodes_to_swap[i + 1].data, nodes_to_swap[i].data

                nodes_to_swap.clear()

            current_level += 1

def print_tree_level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print()  # Move to the next line after each level
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)

print("Original Tree:")
print_tree_level_order(bst.root)

bst.swap_nodes(2)

print("\nTree after swapping nodes at level 2:")
print_tree_level_order(bst.root)
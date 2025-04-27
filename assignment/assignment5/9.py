class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sorte(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = Node(nums[mid])
    root.left = sorte(nums[:mid])
    root.right = sorte(nums[mid + 1:])
    return root

def in_order(root):
    elements = []
    _in_order(root, elements)
    return elements

def _in_order(root, elements):
    if root:
        _in_order(root.left, elements)
        elements.append(root.key)
        _in_order(root.right, elements)

nums = [1, 2, 3, 4, 5, 6, 7]
bst_root = sorte(nums)
print("In-order Traversal of the BST:", in_order(bst_root))

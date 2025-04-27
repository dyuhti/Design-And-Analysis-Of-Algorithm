class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidSequence(root, arr):
    def dfs(node, index):
        # If we reach the end of the array and the node is a leaf, return True
        if index == len(arr) - 1:
            return node is not None and node.val == arr[index] and node.left is None and node.right is None

        # If the current node is None or its value doesn't match the current value in arr, return False
        if node is None or node.val != arr[index]:
            return False

        # Recursively check the left and right subtrees with the next index in arr
        return dfs(node.left, index + 1) or dfs(node.right, index + 1)

    return dfs(root, 0)


# Example usage
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = None
root.left.left.left = None
root.left.left.right = None
root.left.right.left = None
root.left.right.right = TreeNode(1)
arr = [0, 1, 0, 1]
print(isValidSequence(root, arr))  # Output: True

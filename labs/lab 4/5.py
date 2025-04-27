class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

def isValidSequence(root, arr):
    if not root or not arr:
        return False
    if root.val != arr[0]:
        return False
    if len(arr) == 1:
        return not root.left and not root.right
    return isValidSequence(root.left, arr[1:]) or isValidSequence(root.right, arr[1:])

# Example usage:
lst = [0,1,0,0,1,0,None,None,1,0,0]
arr = [0,1,0,1]
root = construct_tree(lst)
print(isValidSequence(root, arr))
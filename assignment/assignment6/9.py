class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodes(head: ListNode) -> ListNode:
    if not head:
        return None

    dummy = ListNode(0)  # Create a dummy node to store the modified list
    dummy.next = head
    prev = dummy
    stack = []  # Stack to keep track of nodes to be kept

    curr = head
    while curr:
        # Remove nodes from the stack that are smaller than the current node
        while stack and stack[-1].val < curr.val:
            stack.pop()

        # If the stack is empty or the top node is greater than the current node
        if not stack or stack[-1].val >= curr.val:
            stack.append(curr)
            prev = curr
        else:
            # Remove the current node by updating the next pointer of the previous node
            prev.next = curr.next

        curr = curr.next

    # Update the next pointers of the nodes in the stack
    for i in range(len(stack) - 1):
        stack[i].next = stack[i + 1]
    stack[-1].next = None  # Set the next pointer of the last node to None

    return dummy.next
# Create the linked list: 5 -> 2 -> 13 -> 3 -> 8
node1 = ListNode(5)
node2 = ListNode(2)
node3 = ListNode(13)
node4 = ListNode(3)
node5 = ListNode(8)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Call the removeNodes function
new_head = removeNodes(node1)

# Print the modified linked list
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
# Output: 13 8
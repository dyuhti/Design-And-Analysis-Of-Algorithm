class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Create a dummy node to handle the case when we need to remove the head
    dummy = ListNode(0)
    dummy.next = head

    # Initialize two pointers
    first = dummy
    second = dummy

    # Move the second pointer n+1 steps ahead
    for _ in range(n + 1):
        if not second.next:
            # If the list has fewer than n+1 nodes, return the original list
            return head
        second = second.next

    # Move both pointers until the second pointer reaches the end
    while second:
        first = first.next
        second = second.next

    # Remove the nth node from the end by skipping its next pointer
    first.next = first.next.next

    return dummy.next


# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# Remove the 2nd node from the end
new_head = removeNthFromEnd(node1, 2)

# Print the modified linked list
current = new_head
while current:
    print(current.val, end=" ")
    current = current.next
# Output: 1 2 3 5
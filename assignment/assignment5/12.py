class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        if curr.next and curr.next.val < curr.val:
            while prev.next and prev.next.val < curr.next.val:
                prev = prev.next
            temp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = temp
            prev = dummy
        else:
            curr = curr.next

    return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

values = [-1, 5, 3, 4, 0]
head = create_linked_list(values)
sorted_head = insertionSortList(head)
print("Sorted Linked List:", linked_list_to_list(sorted_head))

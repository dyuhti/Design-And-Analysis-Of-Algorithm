class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head):
    dummy = ListNode(0)
    curr = head
    while curr:
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        next_temp = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next_temp

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



values = [4, 2, 1, 3]
head = create_linked_list(values)
sorted_head = insertionSortList(head)
print("Sorted Linked List:", linked_list_to_list(sorted_head))

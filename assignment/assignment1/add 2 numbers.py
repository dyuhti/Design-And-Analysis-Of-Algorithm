class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        curr.next = ListNode(digit)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        curr.next = ListNode(carry)

    return dummy.next


def create(values):
    dummy = ListNode()
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


l1 = create([2, 4, 3])
l2 = create([5, 6, 4])

result = add(l1, l2)
while result:
    print(result.val, end="")
    result = result.next

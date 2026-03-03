from typing import Optional
from ListNode import ListNode

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# one, two, three = ListNode(1), ListNode(2), ListNode(3)
# one.next, two.next = two, three

# print(middleNode(one).val)
from list_node import ListNode
from typing import Optional


def has_cycle(head: ListNode) -> Optional[ListNode]:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            ptr1, ptr2 = head, slow

            while ptr1 is not ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            return ptr1
    return None

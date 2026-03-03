from typing import Optional
from list_node import ListNode


def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:
    res = p = ListNode(None)
    p1, p2 = L1, L2

    while p1 and p2:
        if p1.data < p2.data:
            p.next = p1
            p = p.next
            p1 = p1.next
        elif p2.data <= p1.data:
            p.next = p2
            p = p.next
            p2 = p2.next

    while p1:
        p.next = p1
        p = p.next
        p1 = p1.next

    while p2:
        p.next = p2
        p = p.next
        p2 = p2.next

    return res.next

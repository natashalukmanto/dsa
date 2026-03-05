from typing import Optional
from ListNode import ListNode


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    dummy = head.next
    prev = None

    # A -> B -> C -> D -> E
    while head and head.next:
        if prev:
            prev.next = head.next  # A.next = D
        prev = head  # prev = A

        next_node = head.next.next  # save C
        head.next.next = head  # B.next = A

        head.next = next_node
        head = next_node  # head = C

    return dummy


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        next_pair = second.next

        prev.next = second
        second.next = first
        first.next = next_pair

        prev = first

    return dummy.next

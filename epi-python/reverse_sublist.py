from typing import Optional
from list_node import ListNode


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:

    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverses sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next,
            temp,
        )
    return dummy_head.next


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    if not L or not L.next:
        return L

    dummy = sublist_iter = ListNode(0, L)

    for _ in range(1, start):
        sublist_iter = sublist_iter.next

    prev = None
    curr = sublist_iter.next
    tail = curr

    for _ in range(finish - start + 1):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    sublist_iter.next = prev
    tail.next = curr  # curr is node AFTER the sublist

    return dummy.next

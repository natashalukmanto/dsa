from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head

    # find the length of the linkedlist + create a ring
    old_tail, length = head, 1
    while old_tail.next:
        length += 1
        old_tail = old_tail.next
    old_tail.next = head

    new_tail = head
    for i in range(length - k % length - 1):
        new_tail = new_tail.next  # stop right before the head
    new_head = new_tail.next

    new_tail.next = None

    return new_head


def rotateRight0(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None

    length, pointer = 1, head

    while pointer.next:
        pointer = pointer.next
        length += 1

    k %= length
    if k == 0:
        return head

    new_head_index = length - k
    new_head, new_tail = head, ListNode(0, head)
    while new_head_index:
        new_head = new_head.next
        new_tail = new_tail.next
        new_head_index -= 1

    pointer.next = head

    new_tail.next = None

    return new_head

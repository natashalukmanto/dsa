from typing import Optional
from ListNode import ListNode


# Recursive
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:
        return head
    head.next = self.removeElements(head.next, val)
    return head.next if head.val == val else head


# Iterative
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    sentinel = ListNode(0, head)
    prev, curr = sentinel, head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return sentinel.next


def removeElements0(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    curr = head
    prev = dummy

    while prev:
        while curr and curr.val == val:
            prev.next = curr.next
            curr = curr.next
        if curr:
            curr = curr.next
        prev = prev.next

    return dummy.next

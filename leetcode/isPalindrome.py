from typing import Optional
from ListNode import ListNode


def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def reverse(head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    p1, p2 = head, reverse(slow)

    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1, p2 = p1.next, p2.next
    return True


def isPalindrome0(self, head: Optional[ListNode]) -> bool:
    list_node = []
    while head:
        list_node.append(head.val)
        head = head.next

    return list_node == list_node[::-1]

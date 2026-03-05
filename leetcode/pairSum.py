from typing import Optional
from ListNode import ListNode

def pairSum(self, head: Optional[ListNode]) -> int:
    slow = fast = head
    prev = None

    # reverse first half while finding middle
    while fast and fast.next:
        fast = fast.next.next

        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # now:
    # prev = reversed first half
    # slow = start of second half

    ans = 0
    while slow:
        ans = max(ans, prev.val + slow.val)
        prev = prev.next
        slow = slow.next

    return ans

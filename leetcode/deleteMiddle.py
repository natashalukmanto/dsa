from typing import Optional
from ListNode import ListNode

def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return None

    slow = ListNode(0, head)
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    slow.next = slow.next.next
    return head
from ListNode import ListNode
from typing import Optional

def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
    connector, curr = None, head
    group_count = count = 1

    def reverse_between(sentinel, k):
        prev = sentinel
        curr = sentinel.next
        tail = sentinel.next

        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        sentinel.next = prev
        tail.next = curr

        return tail

    while curr:
        if group_count == count or not curr.next:
            if count % 2 == 0:
                curr = reverse_between(connector, count)
            connector = curr
            group_count += 1
            count = 0
        count += 1
        curr = curr.next

    return head

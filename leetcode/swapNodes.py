from ListNode import ListNode
from typing import Optional

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = head
    first_node = end_node = head

    for _ in range(k-1):
        dummy = dummy.next
    first_node = dummy

    while dummy and dummy.next:
        dummy = dummy.next
        end_node = end_node.next

    first_node.val, end_node.val = end_node.val, first_node.val

    return head

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front_node = end_node = None
        current_node = head
        list_length = 0

        while current_node:
            list_length += 1

            if end_node:
                end_node = end_node.next
            
            if list_length == k:
                front_node = current_node
                end_node = head
            
            current_node = current_node.next
        
        front_node.val, end_node.val = end_node.val, front_node.val
    
        return head

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    list_node = []
    while head:
        list_node.append(head.val)
        head = head.next
    
    list_node[-k], list_node[k-1] = list_node[k-1], list_node[-k]

    dummy = ListNode(0, None)
    p = dummy
    for i in list_node:
        p.next = ListNode(i, None)
        p = p.next
    
    return dummy.next
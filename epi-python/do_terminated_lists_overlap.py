from list_node import ListNode

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(l: ListNode) -> int:
        pointer, length = l, 0
        
        while pointer:
            length += 1
            pointer = pointer.next
        
        return length

    l0_length, l1_length = length(l0), length(l1)
    
    if l0_length > l1_length: 
        l0, l1 = l1, l0
        
    for _ in range(abs(l0_length - l1_length)):
        l1 = l1.next
    
    while l1 and l0 and l1 is not l0:
        l1, l0 = l1.next, l0.next    
    
    return l0
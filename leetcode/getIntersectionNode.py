from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    def get_length(node):
        length = 0
        pointer = node
        while pointer:
            length += 1
            pointer = pointer.next
        return (length, pointer)

    lenA, pA = get_length(headA)
    lenB, pB = get_length(headB)

    if pA != pB:
        return None
    else:
        if lenA < lenB:  # A will always be the longer linked list
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        diff = lenA - lenB
        pA, pB = headA, headB
        while diff:
            pA = pA.next
            diff -= 1

        while pA != pB:
            pA = pA.next
            pB = pB.next

        return pA

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    pA, pB = headA, headB

    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next
    
    return pA
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # step 1: get length and tail of any linked list
        length = 1
        tail = head
        while tail.next: # so that tail is the last item and tail.next is None
            tail = tail.next
            length += 1
        
        # step 2: get mod of k
        k %= length
        if k == 0: return head

        # step 3: turn it into a CYCLE. Kind of like making a necklace of beads or something
        tail.next = head

        # step 4: now just BREAK the necklace at the correct place
        # this will give the new tail and head if you find the correct break point
        # correct place is found by looping length - k - 1 times (try to verify)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        # first save new head before "breaking"
        new_head = new_tail.next
        # break it off now
        new_tail.next = None
        return new_head
                    
            
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        last_seen = cur
        while cur:
            if cur.val != last_seen.val:
                last_seen.next = cur
                last_seen = cur
            elif not cur.next:
                last_seen.next = None
            cur = cur.next
        return head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        # delete
        left.next = left.next.next
        return dummy.next
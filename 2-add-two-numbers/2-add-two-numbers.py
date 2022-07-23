# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = []
        overflow = (l1.val + l2.val) // 10
        sum.append((l1.val+ l2.val) % 10)
        while (l1.next != None) or (l2.next != None):
            if l2.next == None:
                y = 0
            else:
                y = l2.next.val
                l2.next = l2.next.next
                
            if l1.next == None:
                x = 0
            else:
                x = l1.next.val
                l1.next = l1.next.next
                
            added = x + y + overflow
            overflow = added // 10
            added = added % 10
            sum.append(added)
        
        if overflow != 0:
            sum.append(1)
            
        rlist = ListNode(sum[0])
        curr = rlist
        # Adding of new nodes
        for i in sum[1:]:
            NewNode = ListNode(i)
            curr.next = NewNode
            curr = NewNode
            
        return rlist 
        
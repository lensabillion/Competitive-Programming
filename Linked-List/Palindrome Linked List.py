# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## find the mid
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        ## reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        ## compare the halfs
        while node:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        return True
            

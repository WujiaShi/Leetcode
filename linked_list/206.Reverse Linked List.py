class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
        return prev
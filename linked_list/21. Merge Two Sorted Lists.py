class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            merge_head = l1
            merge_head.next = self.mergeTwoLists(l1.next, l2)
        else:
            merge_head = l2
            merge_head.next = self.mergeTwoLists(l1, l2.next)
        
        return merge_head
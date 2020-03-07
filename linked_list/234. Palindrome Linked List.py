class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
            
        p1, p2 = head, head
        while p2:
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                p2 = p2.next
        
        mid_head = p1
        prev, cur = None, mid_head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        
        head1, head2 = prev, head
        while head1 and head2:
            if head1.val == head2.val:
                head1 = head1.next
                head2 = head2.next
            else:
                return False
            
        return True
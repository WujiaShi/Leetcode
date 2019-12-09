class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur, length, cur_len = head, 0, 1
        while cur:
            cur, length = cur.next, length + 1
        
        res = ListNode(0)
        res.next = head
        
        # merge the list in different cur_len.
        while cur_len < length:
            pre, cur_head = res, res.next
            while cur_head:
                # get the two merge head `h1`, `h2`
                h1, i = cur_head, cur_len
                while i and cur_head: 
                    cur_head, i = cur_head.next, i - 1
                if i: 
                    break 
                # no need to continue because the `h2` is None.
                h2, i = cur_head, cur_len
                while i and cur_head: 
                    cur_head, i = cur_head.next, i - 1
            
                len_h1, len_h2 = cur_len, cur_len - i 
                # merge the `h1` and `h2`.
                while len_h1 and len_h2:
                    if h1.val < h2.val: 
                        pre.next = h1
                        h1 = h1.next
                        len_h1 -= 1
                    else: 
                        pre.next = h2
                        h2 = h2.next
                        len_h2 -= 1
                    pre = pre.next
                    
                pre.next = h1 if len_h1 else h2
                
                while len_h1 > 0 or len_h2 > 0: 
                    pre = pre.next
                    len_h1 -= 1 
                    len_h2 -= 1
                pre.next = cur_head 
            cur_len *= 2
        return res.next

#solve the question by recursion 
class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        # 找到中点
        slow = head
        fast = head
        # 使用这种方式，当结点个数为 2 个时候，slow 在左结点
        # 不会导致死循环
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        lnode = self.sortList(head)
        rnode = self.sortList(head2)

        return self.__merge_two_sorted_list(lnode, rnode)

    def __merge_two_sorted_list(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.val < head2.val:
            head1.next = self.__merge_two_sorted_list(head1.next, head2)
            return head1
        else:
            head2.next = self.__merge_two_sorted_list(head1, head2.next)
            return head2

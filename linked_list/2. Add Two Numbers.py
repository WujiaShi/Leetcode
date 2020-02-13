class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = self.get_num(l1)
        l2_num = self.get_num(l2)
        num_sum = l1_num + l2_num
        return self.get_linklist(num_sum)
        
    def get_num(self, head):
        digit = []
        num = 0
        while head:
            digit.append(head.val)
            head = head.next
        for i in range(len(digit)):
            num += digit[i] * pow(10, i)
        return num
    
    def get_linklist(self, num):
        num = str(num)
        num = num[::-1]
        dummy = ListNode(-1)
        prev = dummy
        for i in num:
            cur = ListNode(int(i))
            prev.next = cur
            prev = cur
        return dummy.next
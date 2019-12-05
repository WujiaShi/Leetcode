class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
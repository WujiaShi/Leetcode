# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        #copy every node on the original linklist, and attach it after the node
        cur = head
        while cur:
            cur_next = cur.next
            clone = Node(cur.val, None, None)
            cur.next = clone
            clone.next = cur_next
            cur = cur_next
        
        #copy random pointer of each node
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        #deattach copyed nodes from the original linkedlist
        cur = head
        clone_head = head.next
        clone_cur = clone_head
        while clone_cur.next:
            cur.next = cur.next.next
            cur = cur.next
            clone_cur.next = clone_cur.next.next
            clone_cur = clone_cur.next
        #set tail pointer point to None
        cur.next = None
        clone_cur.next = None
        return clone_head
# linklist

# 24. Swap Nodes in Pairs
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None: return None
        if head.next == None: y = head
        if head.next: y = head.next
        while head and head.next and head.next.next and head.next.next.next:
            print('case1')
            head.next.next, head.next, head = head, head.next.next.next, head.next.next
        if head and head.next and head.next.next and head.next.next.next == None:
            print('case2')
            head.next.next, head.next, head = head, head.next.next, head.next.next
        if head and head.next and head.next.next == None:  
            print('case3')
            head.next.next, head.next = head, None 
        return y
# 141. Linked List Cycle
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
# 206 Reverse Linked List    
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
# 876. Middle of the Linked List
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        dic = {}
        cur, prev = head, None
        while cur:
            dic[count] = cur
            count = count + 1
            cur = cur.next
        return dic[int(count/2)]

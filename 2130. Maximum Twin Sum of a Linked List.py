# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if not head or not head.next:
            return 0

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head2 = prev
        Max = 0
        slow = head
        while slow and slow.next:
            Max = max(Max, slow.val+head2.val)
            slow = slow.next
            head2 = head2.next

        return Max

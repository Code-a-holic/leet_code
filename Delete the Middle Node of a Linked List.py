# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dummy_node = ListNode(next=head)
        slow = fast = head
        prev = dummy_node

        while fast and fast.next != None:
            slow = slow.next
            prev = prev.next
            fast = fast.next.next

        prev.next = slow.next
        return dummy_node.next





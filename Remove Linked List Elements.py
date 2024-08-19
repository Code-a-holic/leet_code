# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy_node = ListNode(next=head)
        prev, curr = dummy_node, head

        if head == None:
            return head

        while curr.next != None:
            if curr.val == val:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        if curr.val == val:
            prev.next = None

        return dummy_node.next


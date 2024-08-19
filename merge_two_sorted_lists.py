class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            if list2 is None:
                return list1
            else:
                return list2
        elif list2 is None:
            return list1


        current_node = list1

        count1 = count2 = 0

        while current_node.next is not None:
            count1 += 1
            current_node = current_node.next
        count1 += 1

        current_node = list2

        while current_node.next is not None:
            count2 += 1
            current_node = current_node.next
        count2+=1

        head = ListNode()

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
            head.next = None
        else:
            head=list2
            list2 = list2.next
            head.next = None

        current_node = head

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
                current_node = current_node.next
            else:
                current_node.next = list2
                list2 = list2.next
                current_node = current_node.next

        current_node.next = list1 if list1 is not None else list2

        return head
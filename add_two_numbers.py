class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = num_2 = 0

        arr1 = []
        arr2 = []
        current_node = l1

        while current_node is not None:
            arr1.append(current_node.val)
            current_node = current_node.next

        current_node = l2

        while current_node is not None:
            arr2.append(current_node.val)
            current_node = current_node.next

        for i in range(len(arr1)):
            num_1 = num_1 + (arr1[i] * (10 ** i))

        for i in range(len(arr2)):
            num_2 = num_2 + (arr2[i] * (10 ** i))

        num_2 = num_1 + num_2

        arr2 = []

        if num_2 > 0:
            while num_2 != 0:
                arr2.append(num_2 % 10)
                num_2 = int(num_2 / 10)
        elif num_2 == 0:
            arr2.append(num_2)

        head = None
        current_node = None

        for i in range(len(arr2)):
            new_node = ListNode(val=arr2[i])

            if head == None:
                head = new_node
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node

        return head
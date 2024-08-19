class Solution(object):  #Fastest Soln
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set(nums)

        return (len(set1) - (0 in set1))


class Solution(object): #my soln
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        count = 0
        n = len(nums)

        nums.sort()

        for i in range(len(nums)):

            if nums[i] == 0:
                continue
            else:
                temp = nums[i]
                for j in range(i, len(nums)):
                    nums[j] = nums[j] - temp
                count += 1
                nums.sort()

        return count

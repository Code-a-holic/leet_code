class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        nums.sort()
        while True:
            if i == len(nums):
                break
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        print(nums)


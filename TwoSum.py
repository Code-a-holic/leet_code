class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        input_dict = {}
        for i in range(len(nums)):
            second_num = target - nums[i]
            try:
                if input_dict[second_num] == second_num:
                    for j in range(len(nums)):
                        if nums[j] == second_num:
                            return([j, i])
            except KeyError:
                input_dict[nums[i]] = nums[i]
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for i in nums:
            if i in count:
                res += count[i]
                count[i] += 1
            else:
                count[i] = 1

        return res
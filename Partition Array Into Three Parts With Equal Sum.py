class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        avg = sum(arr) // 3

        count = 0
        sum_temp = 0
        for swi in range(len(arr)):
            sum_temp += arr[swi]
            if sum_temp == avg:
                count += 1
                sum_temp = 0

            if count == 3:
                return True

        return count == 3

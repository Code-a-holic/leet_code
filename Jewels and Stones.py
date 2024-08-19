class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict1 = {}
        count = 0

        for i in jewels:
            dict1[i] = 0

        for i in stones:
            if i in dict1:
                dict1[i] += 1

        for i in dict1.values():
            count += i

        return count
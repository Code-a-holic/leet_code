class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dict1 = {}
        count = 0
        for i in range(len(s)):
            dict1[s[i]] = i

        for i in range(len(t)):
            if t[i] in dict1:
                dict1[t[i]] = abs(dict1[t[i]] - i)

        for i in dict1.values():
            count += i

        return count
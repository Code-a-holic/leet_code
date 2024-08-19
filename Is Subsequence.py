class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while True:
            if i == len(s):
                return True
            elif j == len(t):
                return False
            elif s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        fc = 0

        r = list(s)

        for i in range(len(r)):
            if r[i] == "R":
                count += 1
                if count == 0:
                    fc += 1
            if r[i] == "L":
                count -= 1
                if count == 0:
                    fc += 1

        return fc

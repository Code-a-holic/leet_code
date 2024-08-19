class Solution:
    def isFascinating(self, n: int) -> bool:

        clist = [0] * 10

        if n * 2 > 1000 or n * 3 > 1000:
            return False

        if n % 10 == 0:
            return False

        s = str(n)
        s2 = str(n * 2)
        s3 = str(n * 3)

        for i in range(len(s)):
            clist[int(s[i])] += 1
            clist[int(s2[i])] += 1
            clist[int(s3[i])] += 1

        for i in clist[1:]:
            if i < 1 or i > 1:
                return False

        return True



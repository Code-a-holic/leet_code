class Solution:
    def secondHighest(self, s: str) -> int:
        s1 = list(s)
        if len(s1) == 1:
            return -1
        i = 0

        if not s.isalnum():
            s1 = int(s1)
            while True:
                if i < len(s1):
                    s1[i] = int(s1[i])
                    i += 1
                else:
                    s1.sort()
                    break
        else:
            while True:
                try:
                    if i < len(s1):
                        s1[i] = int(s1[i])
                        i += 1
                    else:
                        s1.sort()
                        break
                except ValueError:
                    s1.pop(i)

        if len(s1) == 0 or len(s1) == 1:
            return -1

        d1 = set(s1)

        if len(d1) == 1:
            return -1
        else:
            s1 = list(d1)
            s1.sort()
            return s1[len(s1) - 2]



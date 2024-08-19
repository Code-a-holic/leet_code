class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        uq_pattern = set(pattern)
        check_list = []
        start = 0
        d1 = {}

        for i in range(len(s)):
            if s[i] == " ":
                check_list.append(s[start:i])
                start = i + 1
        check_list.append(s[start:len(s)])

        # check_list = s.split()

        if len(pattern) != len(check_list):
            return False

        s = set(check_list)
        print(uq_pattern, s)

        if len(uq_pattern) != len(s):
            return False
        else:
            for i in uq_pattern:
                for j in range(len(pattern)):
                    if i == pattern[j]:
                        d1[i] = check_list[j]
                        break

        for i in range(len(pattern)):
            value = d1[pattern[i]]
            print(value, check_list[i])
            if value == check_list[i]:
                continue
            else:
                return False
        return True








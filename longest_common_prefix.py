class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs[0] == "":
            return prefix
        elif len(strs) == 1:
            prefix += strs[0]
            return prefix
        else:
            for i in range(len(strs[0])):
                print(i)
                count = 0
                for j in range(len(strs)):
                    try:
                        if strs[0][i] == strs[j][i]:
                            count += 1
                    except IndexError:
                        return prefix
                if count == len(strs):
                    prefix += strs[0][i]
                else:
                    return prefix
            return prefix
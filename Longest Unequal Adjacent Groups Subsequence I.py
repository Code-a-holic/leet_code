class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev_bit = groups[0]
        i = 1
        while True:
            try:
                if groups[i] == prev_bit:
                    words.pop(i)
                    groups.pop(i)
                else:
                    prev_bit = groups[i]
                    i += 1
            except IndexError:
                return words




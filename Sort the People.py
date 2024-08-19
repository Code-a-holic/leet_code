class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict1 = {}
        for i in range(len(heights)):
            dict1[heights[i]] = names[i]

        heights = sorted(heights, reverse=True)

        return [dict1[heights[i]] for i in range(len(heights))]
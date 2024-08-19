class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # arr_len = len(prices)
        # for i in range(arr_len):
        #     prices[i] = max(prices[i:]) - prices[i]
        # prices.sort()
        # return prices[arr_len - 1]
        l = 0
        h = 1
        current_profit = 0
        while h < len(prices):
            if prices[l] >= prices[h]:
                l = h
                h += 1
            else:
                if current_profit < (prices[h] - prices[l]):
                    current_profit = prices[h] - prices[l]
                h+=1
        return current_profit







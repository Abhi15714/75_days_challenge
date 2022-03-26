class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_profit=0
        curr_profit=0
        while r<len(prices):
            curr_profit=prices[r]-prices[l]
            if prices[l]<prices[r]:
                max_profit=max(curr_profit,max_profit)
            else:
                l=r
            r+=1
        return max_profit
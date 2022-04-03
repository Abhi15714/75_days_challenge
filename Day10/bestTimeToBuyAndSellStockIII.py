class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dpl=[0]*n
        dpl[0]=0
        minprofit=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minprofit:
                minprofit=prices[i]
            dpl[i]=max(dpl[i-1],prices[i]-minprofit)
            
        dpr=[0]*n
        dpr[n-1]=0
        maxprofit=prices[n-1]
        for i in range(n-2,-1,-1):
            if prices[i]>maxprofit:
                maxprofit=prices[i]
            dpr[i]=max(dpr[i+1],maxprofit-prices[i])
            
        ans=-math.inf
        for i in range(n):
            ans=max(ans,dpr[i]+dpl[i])
            
        return ans
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        tot_sum=0
        for i in range(n):
            tot_sum+=cardPoints[i]
        if k==n:
            return tot_sum
        
        size=n-k
        ans=0
        sum=0
        i=0
        for j in range(n):
            sum+=cardPoints[j]
            if j-i+1==size:
                ans=max(ans,tot_sum-sum)
                sum-=cardPoints[i]
                i+=1
                
        return ans
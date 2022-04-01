class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        #maximum area of horizontal will always be the part of it.
        horizontalCuts.sort()
        hmax=horizontalCuts[0]
        n=len(horizontalCuts)
        for i in range(1,len(horizontalCuts)):
            if horizontalCuts[i]-horizontalCuts[i-1]>hmax:
                hmax=horizontalCuts[i]-horizontalCuts[i-1]
                
        if hmax < h-horizontalCuts[n-1]:
            hmax = h-horizontalCuts[n-1]
            
        
        verticalCuts.sort()
        vmax=verticalCuts[0]
        m=len(verticalCuts)
        for i in range(1,m):
            if verticalCuts[i]-verticalCuts[i-1]>vmax:
                vmax=verticalCuts[i]-verticalCuts[i-1]
            
        if vmax < w-verticalCuts[m-1]:
            vmax= w-verticalCuts[m-1]
            
        res=(vmax*hmax)%1000000007
        
        return res
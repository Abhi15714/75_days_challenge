class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        right=[0]*n
        s=[]
        for i in range(n-1,-1,-1):
            while len(s)>0 and s[-1][0]>=heights[i]:
                s.pop()
            if len(s)>0 and s[-1][0]<heights[i]:
                right[i]=s[-1][1]
            else:
                right[i]=n
            s.append([heights[i],i])
            
        left=[0]*n
        t=[]
        for i in range(n):
            while len(t)>0 and t[-1][0]>=heights[i]:
                t.pop()
            if len(t)>0 and t[-1][0]<heights[i]:
                left[i]=t[-1][1]
            else:
                left[i]=-1
            t.append([heights[i],i])
            
        area=[0]*n
        for i in range(n):
            area[i]=heights[i]*(right[i]-left[i]-1)
        
        return max(area)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BROUTE FORCE SOLUTION
        # ans=0
        # for i in range(len(height)):
        #     for j in range(1,len(height)):
        #         area= (j-i)*min(height[i],height[j])
        #         ans=max(ans,area)
        # return ans
        
        l=0
        r=len(height)-1
        ans=0
        while l<r:
            area=(r-l)*min(height[l],height[r])
            ans=max(ans,area)
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:           #edge case when both left and right are equal.
                r-=1        #here we can either move left or right any.
                
        return ans
                        
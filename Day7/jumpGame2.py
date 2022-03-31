class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        l=0
        r=0
        while r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            count+=1
        return count
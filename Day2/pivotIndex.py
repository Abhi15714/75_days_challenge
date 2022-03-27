class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum=sum(nums)
        n=len(nums)
        for i in range(n):
            lsum+=nums[i]
            rsum-=nums[i]
            
            if lsum-nums[i]==rsum:
                return i
        return -1
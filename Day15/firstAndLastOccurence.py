class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        res1=-1

        while l<=r:
            mid= l+(r-l)//2
            if nums[mid]==target:
                res1=mid
                r=mid-1
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
            
        l=0
        r=n-1
        res2=-1        
        while l<=r:
            mid= l+(r-l)//2
            if nums[mid]==target:
                res2=mid
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1

        return res1,res2

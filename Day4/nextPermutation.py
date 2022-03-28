class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        i=len(nums)-1
        key=-1
        while i>0:
            if nums[i]>nums[i-1]:
                key=i-1
                break
            i-=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[key]:
                nums[i],nums[key]=nums[key],nums[i]
                nums[key+1:]=sorted(nums[key+1:])
                return
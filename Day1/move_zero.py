class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        for j in range(len(nums)):
            if nums[j]==0:
                j+=1
            else:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
        return nums
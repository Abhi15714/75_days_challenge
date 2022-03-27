class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        j=n-1
        ls=[0]*n
        l=n-1
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                ls[l]=nums[i]*nums[i]
                l-=1
                i+=1
            else:
                ls[l]=nums[j]*nums[j]
                j-=1
                l-=1
        return ls
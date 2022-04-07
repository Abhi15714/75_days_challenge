class Solution:
    def binary(self, arr, target,l,r):
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                l=mid+1
            elif arr[mid]>target:
                r=mid-1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
            return -1
        n=len(nums)
        l=0
        r=len(nums)-1
        ans=0
        while l<=r:
            mid=l+(r-l)//2
            nextt= (mid+1)%n
            prev= (mid+n-1)%n
            if nums[mid]<=nums[prev] and nums[mid]<nums[nextt]:
                ans= mid
                break
            elif nums[0]<=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        
        res1= self.binary(nums,target,0,ans-1)
        res2= self.binary(nums,target,ans,len(nums)-1)
        
        return max(res1,res2)
        
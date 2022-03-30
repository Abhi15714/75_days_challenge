class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        sum=0
        diff=math.inf
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==target:
                    return target
                elif sum>target:
                    r-=1
                else:
                    l+=1
                if abs(target-sum)<diff:
                    diff=abs(target-sum)
                    ans=sum
                    
        return ans
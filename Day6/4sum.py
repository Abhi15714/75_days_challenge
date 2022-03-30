class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        sum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum=nums[i]+nums[j]+nums[l]+nums[r]
                    if sum == target:
                        result.add((nums[i],nums[j],nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
        return list(result)
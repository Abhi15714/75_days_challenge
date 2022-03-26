class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in range(len(nums)):
            if target-nums[i] in m:
                return [i,m[target-nums[i]]]
            if nums[i] not in m:
                m[nums[i]]=i

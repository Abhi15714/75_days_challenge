class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        m={0:1}         #initialize our dict with 0:1 
        sum=0
        for i in nums:
            sum+=i
            if sum-k in m:
                res+=m[sum-k]
            if sum in m:
                m[sum]+=1
            else:
                m[sum]=1
        return res
        
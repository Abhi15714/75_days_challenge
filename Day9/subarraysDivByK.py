class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        m={0:1}
        sum=0
        res=0
        for i in nums:
            sum=(sum+i)%k
            if sum in m:
                res+=m[sum]
                m[sum]+=1
            else:
                m[sum]=1
                
        return res
            
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 
        res=[]
        for i in nums:
            if i>0:
                res.append(i)
        m={}
        for i in res:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        for i in range(1,len(nums)+1):
            if i in m:
                continue
            else:
                return i
        return len(nums)+1      # this is for worst case when we didn't find first +ve in entire array.
            
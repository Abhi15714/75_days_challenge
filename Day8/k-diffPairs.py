class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # nums[i]-nums[j]==k    --> nums[i]=nums[j]+k
        res=0        
        if k>0:
            for i in d:
                if i+k in d:
                    res+=1
        
        # when k is zero then check frequency of element>1 that give one unique pair
        elif k==0:
            for i in d:
                if d[i]>1:
                    res+=1
        
        return res
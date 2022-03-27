class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m={}
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        # sorted the created hasmap into the descending order using lambda
        ls=dict(sorted(m.items(),key= lambda x:x[1],reverse=True))
        # return the first key form the descending ordered hashmap that gives the ele with heightest frequency
        return list(ls.keys())[0]
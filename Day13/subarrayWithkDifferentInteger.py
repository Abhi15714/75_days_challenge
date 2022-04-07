class Solution:
    def atmost(self, arr,k):
        m=collections.Counter()
        i=0
        res=0
        for j in range(len(arr)):
            if m[arr[j]]==0:    
                k-=1        # means one character has arrive.
            m[arr[j]]+=1
            while k<0:      # when more than k element enter into window.
                m[arr[i]]-=1
                if m[arr[i]]==0:
                    k+=1
                i+=1
            res+=j-i+1
        return res
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k) - self.atmost(nums,k-1)
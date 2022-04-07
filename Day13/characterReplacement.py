class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m={}
        res=0
        l,r=0,0
        for r in range(len(s)):
            if s[r] in m:
                m[s[r]]+=1
            else:
                m[s[r]]=1
            
            while (r-l+1)-max(m.values())>k:
                m[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            
        return res
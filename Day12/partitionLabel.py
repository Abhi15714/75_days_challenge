class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m={}
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]]=i
            else:
                m[s[i]]=i
        
        res=[]
        size,end=0,0
        for i in range(len(s)):
            size+=1
            end=max(end,m[s[i]])
            
            if i==end:
                res.append(size)
                size=0
        return res
            
            
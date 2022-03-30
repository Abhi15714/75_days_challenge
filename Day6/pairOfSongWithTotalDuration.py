class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # BROUTE FORCE
        # count=0
        # n=len(time)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if (time[i]+time[j])%60==0:
        #             count+=1
        # return count
                
        # USING HASHMAP
        for i in range(len(time)):
            time[i]=time[i]%60
            
        d={}
        for i in time:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        ans=0
        for i in d:
            if i==0 or i==30:
                ans+=(d[i]*(d[i]-1))//2
            elif 60-i in d:
                ans+=d[i]*d[60-i]
                d[i]=0
                d[60-i]=0
        return ans
                
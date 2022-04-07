class Solution:
    def binary(self,arr):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]>=0:
                l=mid+1
            else:
                r=mid-1
                      
        return len(arr)-l
    def countNegatives(self, grid: List[List[int]]) -> int:
        # BINARY SEARCH SOLUTION..
        res=0
        for row in grid:
            res+=self.binary(row)
        return res
            
        
        
        
        # boute force
        res=0
        for i in grid:
            for j in i:
                if j<0:
                    res+=1
                    
        return res
        
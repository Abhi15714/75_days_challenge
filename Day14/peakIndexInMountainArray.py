class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # BINARY SERCH..    
        l=0
        r=len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1]:
                l+=1
            else:
                r-=1
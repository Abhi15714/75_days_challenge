class Solution:
    def myPow(self, x: float, n: int) -> float:
        #RECURSIVE SOLUTION
        def recurse(x,n):
            # base cases
            if x==0:
                return 0
            if n==0:
                return 1
            # calling function to half values
            res=recurse(x,n//2)
            res=res*res     # full = half*half
            return x*res if n%2!=0 else res     # if no. is odd and even case
            
            
        res=recurse(x,abs(n))
        return res if n>=0 else 1/res
        
        
        
        
        #return x**n
        
        
        # return pow(x,n)
        
        # BROUTE FORCE
#         res=1
#         for  i in range(abs(n)):
#             if n>0:
#                 res=res*x
                
#             elif n<0:
#                 res=res/x
                
#         return res
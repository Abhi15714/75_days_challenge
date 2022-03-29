class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        top,down,left,right= 0, m-1, 0, n-1     #four pointer at every corner of matrix.
        direction=0
        res=[]
        while left<=right and top<=down:
            if direction==0:        # left to right
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
            
            elif direction==1:      #top to down
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                right-=1
            
            elif direction==2:      #right to left
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            
            elif direction==3:      #down to top
                for i in range(down,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            
            direction = (direction+1)%4
                
        return res
                
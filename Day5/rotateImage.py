class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # in order to do this we have two steps.
        # 1.Transpose of matrix--> column becomes rows
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
        # 2. Reverse that transposed matrix.
        for i in range(n):
            matrix[i]=matrix[i][::-1]
        
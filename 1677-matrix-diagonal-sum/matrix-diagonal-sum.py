class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0

        for i in range(n):
            # Add primary diagonal element
            total_sum += mat[i][i]
            # Add secondary diagonal element
            total_sum += mat[i][n - 1 - i]
            
        # If n is odd, subtract the middle element that was added twice
        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]

        return total_sum
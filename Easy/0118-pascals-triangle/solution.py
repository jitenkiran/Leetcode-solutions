class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        
        for r in range(numRows):
            # Initialize the row with 1s
            row = [1] * (r + 1)
            
            # Fill in the interior elements using the previous row
            for c in range(1, r):
                row[c] = triangle[r - 1][c - 1] + triangle[r - 1][c]
                
            triangle.append(row)
            
        return triangle

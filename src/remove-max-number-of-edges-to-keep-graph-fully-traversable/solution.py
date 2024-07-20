class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        # Initialize the matrix with zeros
        num_rows = len(rowSum)
        num_cols = len(colSum)
        matrix = [[0] * num_cols for _ in range(num_rows)]

        # Loop through all cells of the matrix
        row_index, col_index = 0, 0
        while row_index < num_rows and col_index < num_cols:
            # Set the current cell to the minimum of the remaining sums for the current row and column
            matrix[row_index][col_index] = min(rowSum[row_index], colSum[col_index])

            # Subtract the value just assigned to the matrix cell from both rowSum and colSum
            rowSum[row_index] -= matrix[row_index][col_index]
            colSum[col_index] -= matrix[row_index][col_index]

            # If the current row's sum is now zero, move to the next row
            if rowSum[row_index] == 0:
                row_index += 1
            else:
                # Otherwise, if the current column's sum is now zero, move to the next column
                col_index += 1

        # Return the completed matrix
        return matrix


solution = Solution()
print(solution.restoreMatrix([3, 8], [4, 7]))
print(solution.restoreMatrix([5, 7, 10], [8, 6, 8]))

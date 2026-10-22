class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        result = [[0]*row for _ in range(column)]
        for i in range(0,row):
            for j in range(0,column):
               result[j][i] = matrix[i][j]
        return result 
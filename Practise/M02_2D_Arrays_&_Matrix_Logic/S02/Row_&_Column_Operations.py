
#1351. Count Negative Numbers in a Sorted matrix
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        '''
        count=0
        for row in grid:
            for ele in row :
                if ele <0 :
                    count+=1
        return count
        '''
        count=0
        rows,cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]<0:
                    count+=(cols-c)
                    break
        return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(Solution().countNegatives(grid))

'''
#832. Flip an Image
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1-row[i]
        return image
image = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(image))
'''

'''
#54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))
'''
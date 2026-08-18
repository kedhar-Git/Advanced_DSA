#74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        arr = []
        for row in matrix:
            arr+=row
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
        '''
        m,n = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))

#240. Search a 2D Matrix II
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        for row in matrix:
            if target in row:
                return True
        return False
        '''
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1
        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(Solution().searchMatrix(matrix, target))


#378. Kth Smallest Element in a Sorted Matrix
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        '''
        arr = []
        for row in matrix:
            arr+=row
        arr.sort()
        return arr[k-1]
        '''
        import heapq
        min_heap = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(min_heap, matrix[r][c])
        for _ in range(k - 1):
            heapq.heappop(min_heap)
        return min_heap[0]
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(Solution().kthSmallest(matrix, k))


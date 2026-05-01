class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break
        
        #if not (r <= l): return False

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            m = (left + right) // 2
            if matrix[mid][m] > target:
                right = m - 1
            elif matrix[mid][m] < target:
                left = m + 1
            else:
                return matrix[mid][m] == target
        return False
                
        
from typing import List

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3

m_row = (len(matrix))//2
# print(matrix[m_row][0])

# print(matrix[m_row][len(matrix[m_row])-1])

# if matrix[m_row][0] <= target <= matrix[m_row][len(matrix[m_row])-1]:
#     print("yes")

print(matrix[m_row+1::])
print(matrix[:m_row:])

class Solution:
    # li: 1d list

    # binary search
    def bs(self, li, target):
        # base case
        if len(li) == 0:
            return False
        # get the middle index
        m = (len(li))//2
        # get the middle value (val)
        val = li[m]

        if val == target:
            return True
        
        if val < target:
            return self.bs(li[m+1::], target)
        elif val > target:
            return self. bs(li[:m:], target)


    # find the 1d list we looking for and just call bs function
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # no index out of range error for line 30
        if len(matrix) == 0:
            return False

        m_row = (len(matrix))//2

        # no index out of range error for below (line 30 onwards)
        if len(matrix[m_row]) == 0:
            return False

        if matrix[m_row][0] <= target <= matrix[m_row][len(matrix[m_row])-1]:
            li = matrix[m_row]
            return self.bs(li, target)
        
        if target < matrix[m_row][0]:
            return self.searchMatrix(matrix[:m_row:], target)
        elif target > matrix[m_row][len(matrix[m_row])-1]:
            return self.searchMatrix(matrix[m_row+1::], target)



        
        

        
        
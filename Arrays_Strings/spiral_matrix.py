"""Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""


class solution():
    def spiral_matrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        up_wall, right_wall, down_wall, left_wall = 0, n, m, -1

        up , right, down, left = 1, 2, 3, 4 
        """ We ca take actual strings and assign to the direction, but 
            everytime we update direction a new string will be created, hence we take them as variables"""
        
        direction = right
        output = []
        i = j = 0
        while len(output) != m*n :
            if direction == right:
                while j < right_wall:
                    output.append(matrix[i][j])
                    j += 1
                i , j = i+1, j-1
                right_wall -= 1
                direction = down

            elif direction == down:
                while i < down_wall:
                    output.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                down_wall -= 1
                direction = left

            elif direction == left:
                while j > left_wall:
                    output.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                left_wall += 1
                direction = up

            else:
                while i > up_wall:
                    output.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                up_wall += 1
                direction = right
        
        return output


import unittest

def zero_matrix(matrix):
    """
    if one element is zero then the entire row and column are zero
    :param matrix: M * N array
    :return: M * N array
    """
    col = len(matrix)
    row = len(matrix[0])
    first_row = False
    first_col = False

    for i in range(row):
        if matrix[0][i] == 0:
            first_row = True

    for i in range(col):
        if matrix[i][0] == 0:
            first_col = True

    for i in range(1, col):
        for j in range(1, row):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, row):
        if matrix[0][i] == 0:
            for j in range(col):
                matrix[j][i] = 0

    for i in range(1, col):
        if matrix[i][0] == 0:
            for j in range(row):
                matrix[i][j] = 0

    if first_row:
        for i in range(row):

            matrix[0][i] = 0
    if first_col:
        for i in range(col):
            matrix[i][0] == 0

    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
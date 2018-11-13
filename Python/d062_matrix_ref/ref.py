""" This module provides a function named rref() which will take in a matrix
    and change the input matrix. The final result will be the reduced row 
    echelon form of the matrix. The main rref() function uses the other three 
    functions _row_switching(), _reduce_rows(), _cancel_out_pivot_cols() for 
    the number of rows that the matrix has. """

def print_matrix(matrix):
    """ Utility function for printing out a matrix without extra commas or
    brackets anywhere (avoids the standard list printing representation) """
    print()
    for row in matrix:
        for num in row:
            print(num, end=' ')
        print()
    print()

def _row_switching(matrix):
    """ Performs possibly several row switching operations to bring zero rows
    to the bottom of the matrix and rows with pivot positions that are earlier
    than other rows' pivot positions to the top """
    matrix.sort(reverse=True)

def _reduce_rows(matrix):
    """ Reduce the values in each matrix row so that the leading entry is 0.
    This makes it easier to clear out extra numbers in pivot columns later """
    for row_num,row in enumerate(matrix):
        if not all(num == 0 for num in row):
            leading_entry = next(num for num in row if num != 0)
            matrix[row_num] = [num / leading_entry for num in matrix[row_num]]

    # print("Row reduction: ")
    # print_matrix(matrix)

def _cancel_out_pivot_cols(matrix):
    """ Use the leading entries of higher rows to cancel out leading entries of
    the lower rows. All leading entries will be 1, guaranteed by the 
    reduce_rows function above.
    """
    pivot_found = False
    row = -1
    col = -1
    while not pivot_found and row != len(matrix):
        row += 1

        if not all(i == 0 for i in matrix[row]):
            leading_entry_col = next(i for i, x in 
                                    enumerate(matrix[row]) if x != 0)
            # print(f"Col: {leading_entry_col}")
            # print(f"Row: {row}")
        else:
            return
        
        for i in range(row + 1, len(matrix)):
            if matrix[i][leading_entry_col] != 0:
                pivot_found = True

    # print(f'Row: {row}')
    if pivot_found:
        for i in range(0, len(matrix)):
            if matrix[i][leading_entry_col] != 0:
                scalar = 1/matrix[i][leading_entry_col]
                # print(f'Scalar: {scalar}')
                matrix[i] = [scalar * k - l if row != i else l 
                             for k, l in zip(matrix[i], matrix[row])]

    # print("Cancel out rows: ")
    # print_matrix(matrix)


def rref(matrix) -> None:
    """ Pass in a matrix, and this function will take care of the row 
    reduction. As mentioned above, this function checks if the matrix is valid 
    by checking that is of a rectangular shape, and then will loop over the 
    number of rows in the matrix while performing all three row operations in 
    order of switching, multiplication, and 
    """
    base_len = len(matrix[0]) # The length of any one of the matrix's rows
    if not all(len(row) == base_len for row in matrix):
        raise TypeError('Input argument is not a matrix, all rows\' lengths '
                        'must match and all columns\' lengths must match')

    print('Starting matrix:')
    print_matrix(matrix)

    for _ in range(0, len(matrix)):
        _row_switching(matrix)
        _reduce_rows(matrix)
        _cancel_out_pivot_cols(matrix)

    print('Ending matrix:')
    print_matrix(matrix)

def main():
    a = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [0, 1, 0, 1, 0]]
    rref(a)

    b = [[1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 2, 3], [0, 1, 2, 3]]
    rref(b)


if __name__ == '__main__':
    main()
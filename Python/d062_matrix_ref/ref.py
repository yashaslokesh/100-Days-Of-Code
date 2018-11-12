
def print_matrix(matrix):
    print()
    for row in matrix:
        for num in row:
            print(num, end=' ')
        print()
    print()

def row_replacement(matrix):
    matrix.sort(reverse=True)
    # print("Row switching: ")
    # print_matrix(matrix)

def reduce_rows(matrix):
    for row_num,row in enumerate(matrix):
        if not all(num == 0 for num in row):
            leading_entry = next(num for num in row if num != 0)
            matrix[row_num] = [num / leading_entry for num in matrix[row_num]]

    # print("Row reduction: ")
    # print_matrix(matrix)

def cancel_out_rows(matrix):
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
                matrix[i] = [scalar * k - l if row != i else l for k, l in zip(matrix[i], matrix[row])]

    # print("Cancel out rows: ")
    # print_matrix(matrix)


def rref(matrix):
    """
        Pass in a matrix, and this function will take care of the transformation.
    """
    base_len = len(matrix[0]) # The length of any one of the matrix's rows
    if not all(len(row) == base_len for row in matrix):
        raise TypeError('Input argument is not a matrix, all rows\' lengths '
                        'must match and all columns\' lengths must match')

    print("Starting matrix: ")
    print_matrix(matrix)
    # Sort matrix in reverse order, putting rows with zeroes at beginning at the bottom

    for _ in range(0, len(matrix)):
        row_replacement(matrix)
        reduce_rows(matrix)
        cancel_out_rows(matrix)

def main():
    a = [[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [0, 1, 0, 1, 0]]
    rref(a)
    print_matrix(a)

    b = [[1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 2, 3], [0, 1, 2, 3]]
    rref(b)
    print_matrix(b)


if __name__ == '__main__':
    main()
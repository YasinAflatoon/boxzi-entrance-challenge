def matrix_search(matrix, key):
    if not matrix or not matrix[0]:
        return False

    mid_index = len(matrix) // 2

    if key in matrix[mid_index]:
        return True

    elif key < matrix[mid_index][0]:
        return matrix_search(matrix[:mid_index], key)

    else:
        return matrix_search(matrix[mid_index + 1:], key)



mat = [
    [1, 3, 5],
    [7, 8, 10],
    [12, 15, 18]
]

print(matrix_search(mat, 8))   # outputs True
print(matrix_search(mat, 11))   # outputs False

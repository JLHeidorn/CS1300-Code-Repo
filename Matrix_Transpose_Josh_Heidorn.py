def transpose(matrix):
    result = []

    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)

    return result


# Tests
m1 = [[1, 2, 3],
      [4, 5, 6]]
print(transpose(m1))  

#Expected output [[1, 4], [2, 5], [3, 6]]

m2 = [[1, 2],
      [3, 4],
      [5, 6]]
print(transpose(m2))  

#Expected output is [[1, 3, 5], [2, 4, 6]]
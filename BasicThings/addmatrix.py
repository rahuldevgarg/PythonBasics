rows = int(input("Enter the number of rows : "))
col = int(input("Enter the number of col : "))


def take_input():
    mat = []
    for r in range(rows):
        temp = []
        for c in range(col):
            temp.append(int(input("Enter the value at index[{}{}] : ".format(r + 1, c + 1))))
        mat.append(temp)
    return mat


print("Enter Values of Matrix 1")
mat1 = take_input()
print("Enter Values of matrix 2")
mat2 = take_input()


def add_matrix(m, m2):
    mat = []
    for r in range(rows):
        temp = []
        for c in range(col):
            temp.append(m[r][c] + m2[r][c])
        mat.append(temp)
    return mat


res = add_matrix(mat1, mat2)
for i in res:
    print(*i)


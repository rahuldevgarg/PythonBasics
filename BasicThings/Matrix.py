# 1. Matrix Creation
# 2. Matrix Validation
# 3. Matrix Arithmetic Operation
# 4. Matrix Rotation transpose, rotation
rows = int(input("Enter the number of rows : "))
col = int(input("Enter the number of col : "))
h = []
for r in range(rows):
    temp = []
    for c in range(col):
        temp.append(int(input("Enter the value at index[{}{}] : ".format(r+1, c+1))))
    h.append(temp)


# print('Number Of Rows: {}'.format(len(h)))
# print('Number Of Columns: {}'.format(len(h[0])))

for i in h:
    print(*i)

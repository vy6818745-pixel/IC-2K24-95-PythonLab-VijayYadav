mat = []
for r in range(3):
    row = []
    for c in range(3):
        v = int(input("Value row " + str(r + 1) + " col " + str(c + 1) + ": "))
        row.append(v)
    mat.append(row)

print("Matrix:")
for row in mat:
    for v in row:
        print(v, end=" ")
    print()

all_sum = 0
diag_sum = 0
big = mat[0][0]
small = mat[0][0]
for r in range(3):
    for c in range(3):
        all_sum = all_sum + mat[r][c]
        if r == c:
            diag_sum = diag_sum + mat[r][c]
        if mat[r][c] > big:
            big = mat[r][c]
        if mat[r][c] < small:
            small = mat[r][c]

print("Sum all:", all_sum)
print("Sum diagonal:", diag_sum)
print("Largest:", big, "Smallest:", small)
print("Transpose:")
for c in range(3):
    for r in range(3):
        print(mat[r][c], end=" ")
    print()

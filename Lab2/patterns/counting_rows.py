rows = int(input("Rows: "))
for r in range(1, rows + 1):
    for c in range(1, r + 1):
        print(c, end=" ")
    print()

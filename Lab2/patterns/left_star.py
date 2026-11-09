rows = int(input("Rows: "))
for r in range(1, rows + 1):
    for c in range(r):
        print("*", end="")
    print()

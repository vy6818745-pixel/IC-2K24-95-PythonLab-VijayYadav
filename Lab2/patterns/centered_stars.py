rows = int(input("Rows: "))
for r in range(1, rows + 1):
    spaces = rows - r
    print(" " * spaces, end="")
    stars = 2 * r - 1
    for s in range(stars):
        print("*", end="")
    print()

n = int(input("Half width n: "))
for i in range(1, n + 1):
    stars = "*" * i
    gap = " " * (2 * (n - i))
    print(stars + gap + stars)
for i in range(n - 1, 0, -1):
    stars = "*" * i
    gap = " " * (2 * (n - i))
    print(stars + gap + stars)

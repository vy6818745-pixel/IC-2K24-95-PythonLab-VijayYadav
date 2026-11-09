n = int(input("Odd number n: "))
mid = n // 2
for i in range(n):
    if i <= mid:
        left = mid - i
        inner = 2 * i - 1
        if i == 0:
            print(" " * left + "*")
        else:
            print(" " * left + "*" + " " * inner + "*")
    else:
        j = n - 1 - i
        left = mid - j
        inner = 2 * j - 1
        print(" " * left + "*" + " " * inner + "*")

n = int(input("Number: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s = s + i
if s == n:
    print(n, "is perfect")
else:
    print(n, "is not perfect")

limit = int(input("Perfect numbers up to: "))
for n in range(1, limit + 1):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    if s == n and n > 0:
        print(n)

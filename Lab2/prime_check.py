n = int(input("Number: "))
ok = True
if n < 2:
    ok = False
else:
    for d in range(2, n):
        if n % d == 0:
            ok = False
            break
if ok:
    print(n, "is prime")
else:
    print(n, "is not prime")

upto = int(input("Print primes up to: "))
for n in range(2, upto + 1):
    ok = True
    for d in range(2, n):
        if n % d == 0:
            ok = False
            break
    if ok:
        print(n, end=" ")
print()

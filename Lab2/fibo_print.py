count = int(input("How many terms: "))
a = 0
b = 1
for i in range(count):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()

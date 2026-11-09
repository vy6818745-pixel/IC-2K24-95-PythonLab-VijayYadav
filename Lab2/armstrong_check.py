num = int(input("Number: "))
copy = num
power = len(str(num))
total = 0
while copy > 0:
    d = copy % 10
    total = total + d ** power
    copy = copy // 10
if total == num:
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")

start = int(input("Range start: "))
end = int(input("Range end: "))
for num in range(start, end + 1):
    copy = num
    power = len(str(num))
    total = 0
    while copy > 0:
        d = copy % 10
        total = total + d ** power
        copy = copy // 10
    if total == num:
        print(num)

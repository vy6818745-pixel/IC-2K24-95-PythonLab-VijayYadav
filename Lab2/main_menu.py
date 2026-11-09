while True:
    print("1 Armstrong  2 Prime  3 Perfect  4 Palindrome  5 Fibonacci  6 Exit")
    ch = input("Choice: ")
    if ch == "6":
        break
    if ch == "1":
        num = int(input("Number: "))
        copy = num
        p = len(str(num))
        t = 0
        while copy > 0:
            t = t + (copy % 10) ** p
            copy = copy // 10
        print("Armstrong" if t == num else "Not Armstrong")
    elif ch == "2":
        n = int(input("Number: "))
        ok = n >= 2
        for d in range(2, n):
            if n % d == 0:
                ok = False
        print("Prime" if ok else "Not prime")
    elif ch == "3":
        n = int(input("Number: "))
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s = s + i
        if s == n:
            print("Perfect")
        else:
            print("Not perfect")
    elif ch == "4":
        w = input("Word: ")
        print("Palindrome" if w == w[::-1] else "Not palindrome")
    elif ch == "5":
        k = int(input("Terms: "))
        a, b = 0, 1
        for i in range(k):
            print(a, end=" ")
            a, b = b, a + b
        print()
    else:
        print("Wrong choice")

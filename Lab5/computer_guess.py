lo = int(input("Low: "))
hi = int(input("High: "))
print("Think of a number between", lo, "and", hi)
steps = 0
while lo <= hi:
    mid = (lo + hi) // 2
    steps = steps + 1
    print("My guess:", mid)
    hint = input("Type H high, L low, C correct: ").lower()
    if hint == "c":
        print("Got it in", steps, "guesses")
        break
    if hint == "h":
        hi = mid - 1
    elif hint == "l":
        lo = mid + 1
    else:
        print("Use H, L, or C")

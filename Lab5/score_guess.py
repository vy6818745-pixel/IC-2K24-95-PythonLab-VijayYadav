import random

ans = random.randint(1, 100)
points = 100
for attempt in range(10):
    g = int(input("Guess 1-100: "))
    if g == ans:
        print("Right! Score:", points)
        break
    points = points - 10
    if g < ans:
        print("Too small")
    else:
        print("Too big")
    if ans % 2 == 0:
        print("Hint: even")
    else:
        print("Hint: odd")
else:
    print("Game over. Number was", ans)

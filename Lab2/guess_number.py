import random

secret = random.randint(1, 100)
tries = 0
max_tries = 7
while tries < max_tries:
    g = int(input("Guess 1-100: "))
    tries = tries + 1
    if g == secret:
        print("You won in", tries, "tries")
        break
    if g < secret:
        print("Higher")
    else:
        print("Lower")
else:
    print("Lost. Answer was", secret)

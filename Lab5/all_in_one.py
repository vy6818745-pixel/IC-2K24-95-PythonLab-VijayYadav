import random


def run_atm():
    bal = 1000
    if input("PIN (1234): ") != "1234":
        print("Wrong PIN")
        return
    while True:
        print("1 Bal 2 Add 3 Take 4 Back")
        c = input("> ")
        if c == "4":
            return
        if c == "1":
            print(bal)
        elif c == "2":
            bal = bal + int(input("Amount: "))
        elif c == "3":
            w = int(input("Amount: "))
            if w <= bal:
                bal = bal - w
        else:
            print("?")


def run_grades():
    s = 0
    for i in range(5):
        s = s + float(input("Mark: "))
    a = s / 5
    print("Avg", a)


def run_game():
    x = random.randint(1, 50)
    for i in range(5):
        if int(input("Guess 1-50: ")) == x:
            print("OK")
            return
    print("Answer", x)


while True:
    print("1 ATM  2 Grades  3 Guess  4 Exit")
    pick = input("> ")
    if pick == "1":
        run_atm()
    elif pick == "2":
        run_grades()
    elif pick == "3":
        run_game()
    elif pick == "4":
        break

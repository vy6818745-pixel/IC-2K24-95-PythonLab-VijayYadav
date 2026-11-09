money = 5000
correct_pin = "1234"
pin = input("PIN: ")
if pin != correct_pin:
    print("Bad PIN")
else:
    while True:
        print("1 Balance  2 Deposit  3 Withdraw  4 Quit")
        op = input("Pick: ")
        if op == "4":
            break
        if op == "1":
            print("Balance:", money)
        elif op == "2":
            amt = int(input("Deposit amount: "))
            money = money + amt
            print("Done. Balance:", money)
        elif op == "3":
            amt = int(input("Withdraw amount: "))
            if amt > money:
                print("Not enough money")
            else:
                money = money - amt
                print("Done. Balance:", money)
        else:
            print("Try again")

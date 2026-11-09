n = int(input("Number: "))
old = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if old == rev:
    print(old, "is palindrome number")
else:
    print(old, "is not palindrome number")

word = input("Word: ")
if word == word[::-1]:
    print(word, "is palindrome word")
else:
    print(word, "is not palindrome word")

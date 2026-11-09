total = 0
for sub in range(5):
    m = float(input("Marks subject " + str(sub + 1) + ": "))
    total = total + m
avg = total / 5
if avg >= 90:
    g = "A"
elif avg >= 75:
    g = "B"
elif avg >= 60:
    g = "C"
elif avg >= 40:
    g = "D"
else:
    g = "F"
print("Average:", avg)
print("Grade:", g)

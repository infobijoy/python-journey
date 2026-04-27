#Profit Tool
print("=== Profit Calculator ===")
income = int(input("Income: "))
expense = int(input("Expense: "))

profit = income - expense

if profit > 0:
    print("Profit =", profit)
else:
    print("Loss or Zero")
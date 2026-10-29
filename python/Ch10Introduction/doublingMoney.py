# -- doublingMoney.py --
# -- 10.9 Algorithm Design --
# -- Problem: How many years to double $10,000 in an account earning 5% interest per year? --
# -- Set year to 0 --
# -- Set balance to 10000 --
# -- While the balance is less than 20000 --
#   -- Add 1 to the year --
#   -- Set the interest to balance * 0.05 --
#   -- Add the interest to the balance --
# -- Report year as the answer --
year = 0
balance = 10000
while balance < 20000: # the loop will run until the balance is >= 20,000
    year += 1
    interest = balance * 0.05
    balance += interest
print("Years to double:", year)
print("Final balance:", f"{balance:.2f}")
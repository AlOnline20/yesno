import random

tokens = ("unicorn", "horse", "horse", "horse", "horse", "horse", "horse", "donkey", "donkey", "donkey", "donkey", "donkey", "donkey", "zebra", "zebra", "zebra", "zebra", "zebra", "zebra", "zebra")
STARTING_BALANCE = 100

balance = STARTING_BALANCE
for item in range(0,20):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print("Starting Balance: ${:.2f} ".format(STARTING_BALANCE))
print("Final Balance: ${:.2f} ".format(balance))

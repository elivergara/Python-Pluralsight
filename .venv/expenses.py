expenses = [10.5, 8, 5, 15, 20, 5, 3]

agg = 0
for i in expenses:
    agg = agg+ i
print(f"You spent ${agg:.2f}")

# Or...

total = sum(expenses)
print(f"You spent ${total:.2f}")

#################################################




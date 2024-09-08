#6
#6.1
friends = ["Michael", "Ernest", "Dorothy", "Kelvin", "Maxwell", "Addison", "Harrison"]
friend_tuple = [(i, len(i)) for i in friends ]
print(friend_tuple)

#6.2
# Step 2: Create dictionaries for your expenses and your partner's expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate the total expenses for you and your partner
your_total_expenses = sum(your_expenses.values())
partner_total_expenses = sum(partner_expenses.values())

# Print the total expenses
print("\nYour total expenses: $", your_total_expenses)
print("Your partner's total expenses: $", partner_total_expenses)

# Determine who spent more money overall
if your_total_expenses > partner_total_expenses:
    print("\nYou spent more overall.")
elif your_total_expenses < partner_total_expenses:
    print("\nYour partner spent more overall.")
else:
    print("\nBoth of you spent the same amount.")

# Find the expense category where there's a significant difference in spending
print("\nDifference in each category:")
for category in your_expenses:
    your_spending = your_expenses[category]
    partner_spending = partner_expenses[category]
    difference = abs(your_spending - partner_spending)
    if difference > 0:
        print(f"{category}: Difference of ${difference}")

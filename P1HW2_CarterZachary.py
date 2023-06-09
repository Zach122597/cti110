
# Travel Expense Calculator

# 6/8/23

# CTI-110 P1HW2 - Travel Expense

# Zachary Carter

#


budget = float(input("Enter your budget: $"))


destination = input("Enter your travel destination: ")


gas_expense = float(input("Enter the amount you will spend on gas: $"))


accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))


food_expense = float(input("Enter the amount you will spend on food: $"))


total_expenses = gas_expense + accommodation_expense + food_expense


remaining_budget = budget - total_expenses
print()

print("-------------Travel Expenses--------------")


print("Location:", destination)
print("Initial Budget: $", format(budget, ".2f"))
print()
print("Fuel Expense: $", format(gas_expense, ".2f"))
print("Accommodation Expense: $", format(accommodation_expense, ".2f"))
print("Food Expense: $", format(food_expense, ".2f"))
print()
print("Total Expenses: $", format(total_expenses, ".2f"))
print("Remaining Budget: $", format(remaining_budget, ".2f"))

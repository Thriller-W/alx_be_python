## User input for Financial Details
monthly_income = int(input("Enter your monthly income "))
monthly_expenses = int(input("Enter your total monthly expenses "))

## Calculations for Monthly savings
monthly_savings = monthly_income - monthly_expenses

## Projection of Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

## Results
print(f"Your monthly savings are ${monthly_savings:,}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:,.0f}.")

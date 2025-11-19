import csv
import os

def budget():
    
    print("Budget Tracker\nTrack your Income and Expenses by providing Income and Expenses")

    # Input data
    income = float(input("Income (Amount): "))
    expense = float(input("Expense (Amount): "))

    print("")
    
    # Process
    total = income - expense   # Profit/Loss
    sum_total = income + expense  # Just income + expense

    # Percentages
    total_income_expense = income + expense

    percent_income = (income / total_income_expense) * 100 if total_income_expense != 0 else 0
    percent_expense = (expense / total_income_expense) * 100 if total_income_expense != 0 else 0

    # Check if file exists
    file_exists = os.path.isfile("tracker.csv")

    # Save to CSV in append mode
    with open("tracker.csv", "a", newline="") as file:
        writer = csv.writer(file)

        # Write header ONLY if file is new/empty
        if not file_exists:
            writer.writerow(["Income", "Expense", "Total(+)", "Profit/Loss", "Income(%)", "Expense(%)"])

        # Write the data row
        writer.writerow([
            income,
            expense,
            sum_total,
            total,
            round(percent_income, 2),
            round(percent_expense, 2)
        ])

    # Display Summary
    print(f"Total (Income + Expense): R{sum_total}")

    if total < 0:
        print(f"You have a DEFICIT of -R{abs(total)}")
    elif total == 0:
        print("No excess/deficit: R0")
    else:
        print(f"You have an EXCESS of R{total}")

    print(f"Income Percentage: {round(percent_income, 2)}%")
    print(f"Expense Percentage: {round(percent_expense, 2)}%")

budget()

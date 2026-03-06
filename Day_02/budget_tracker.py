def calculate_flexible_budget():
    print("--- Dynamic Monthly Budget Tracker (LKR) ---")
    
    LOW_FUNDS_LIMIT = 500
    total_expenses = 0
    
    try:
        # Get total budget once
        budget_input = input("Enter your total monthly budget (LKR): ").replace(',', '')
        total_budget = float(budget_input)
        
        print("\nEnter your expenses one by one.")
        print("Type 'done' when you are finished.")
        
        # Loop until the user types "done"
        while True:
            user_input = input("Enter expense amount (or 'done'): ").strip().lower()
            
            if user_input == 'done':
                break
            
            try:
                expense_val = float(user_input.replace(',', ''))
                total_expenses += expense_val
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
        
        # Calculate remaining balance
        remaining_balance = total_budget - total_expenses
        
        # Display final results
        print("\n" + "="*30)
        print(f"Total Budget:      {total_budget:,.2f} LKR")
        print(f"Total Expenses:    {total_expenses:,.2f} LKR")
        print(f"Remaining Balance: {remaining_balance:,.2f} LKR")
        
        if remaining_balance < LOW_FUNDS_LIMIT:
            print("Warning: Low Funds")
        print("="*30)
            
    except ValueError:
        print("Error: Initial budget must be a valid number.")

if __name__ == "__main__":
    calculate_flexible_budget()
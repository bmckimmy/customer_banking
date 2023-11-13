# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter savings balance: "))
    savings_interest_rate = float(input("Enter savings interest rate: "))
    savings_months = int(input("Enter the number of months for savings: "))
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_balance_savings, interest_earned_savings = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("Savings Account Summary:")
    print(f"Interest Earned: ${interest_earned_savings:,.2f}")
    print(f"Updated Savings Account Balance: ${updated_balance_savings:,.2f}")
        
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter CD balance: "))
    cd_interest_rate = float(input("Enter CD interest rate: "))
    cd_months = int(input("Enter the number of months for CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_balance_cd, interest_earned_cd = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("CD Account Summary:")
    print(f"Interest Earned: ${interest_earned_cd:,.2f}")
    print(f"Updated CD Account Balance: ${updated_balance_cd:,.2f}")
    
if __name__ == "__main__":
    # Call the main function.
    main()
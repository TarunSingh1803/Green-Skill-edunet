from Banking.account import SavingsAccount, CurrentAccount
from Banking.transaction import deposit, withdraw

accounts = {}  # Dictionary to store accounts with account number as key
def create_account():
    # Create a new account based on user input
    name = input("Enter your name: ").strip()
    acc_type = input("Enter account type (savings/current): ").strip().lower()
    initial_deposit = float(input("Enter initial deposit amount: "))
    if acc_type == "savings":
        account = SavingsAccount(name, initial_deposit)
    elif acc_type == "current":
        account = CurrentAccount(name, initial_deposit)
    else:
        print("Invalid account type. Please try again.")
        return None

    accounts[account.account_number] = account
    print(f"Account created successfully! Account Number: {account.account_number}")
    return account

def login():
    # Login to an existing account
    account_number = int(input("Enter your account number: "))
    if account_number in accounts:
        user_account = accounts[account_number]
        print(f"Welcome {user_account.name} to the SBI Bank!")
        # str1 = str1.center(100,"*")
        # print()
        # print(str1)
        # print()

        while True:
            # print("\nOptions:")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            if isinstance(user_account, SavingsAccount):
                print("4. Calculate Interest")
            print("5. Logout")
            
            choice = input("Choose an option: ")
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                deposit(user_account, amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_account, amount)
            elif choice == '3':
                print(f"Current Balance: {user_account.get_balance()}")
            elif choice == '4' and isinstance(user_account, SavingsAccount):
                user_account.calculate_interest()
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid action. Please try again.")
            user_account.display_balance()
    else:
        print("Account not found. Please create an account first.")
        return None

# Main program loop
def main():
    print("Welcome to the SBI Bank".center(50))
    print("Nagpur SIT Branch".center(50))
    
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using SBI Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please try again...")
            
if __name__ == "__main__":
    main()
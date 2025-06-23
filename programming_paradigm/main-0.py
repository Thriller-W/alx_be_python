import sys
from bank_account import BankAccount

def main():
    # Initial balance of $100
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]

    # Command and amount
    if ':' in command_input:
        command, amount_str = command_input.split(':')
        try:
            amount = float(amount_str)
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)
    else:
        command = command_input
        amount = None

    # Perform the operation
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

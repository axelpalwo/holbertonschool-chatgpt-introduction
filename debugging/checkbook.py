class Checkbook:
    """
    A class to represent a checkbook for managing a user's balance with deposit and withdrawal functionality.
    
    Attributes:
        balance (float): The current balance of the checkbook.
    """

    def __init__(self):
        """
        Initialize a new Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.
        
        Args:
            amount (float): The amount to be deposited.
        
        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook if sufficient funds are available.
        
        Args:
            amount (float): The amount to be withdrawn.
        
        Raises:
            ValueError: If the withdrawal amount is negative.
            ValueError: If there are insufficient funds for the withdrawal.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.
        
        Returns:
            float: The current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))
        return self.balance


def main():
    """
    Main function to handle user interactions for the Checkbook.
    
    Provides options to deposit money, withdraw money, check the balance, or exit the application.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError as e:
                print(f"Error: {e}")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError as e:
                print(f"Error: {e}")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

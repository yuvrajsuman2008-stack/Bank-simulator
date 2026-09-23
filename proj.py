import time

class BankSimulator:
    def __init__(self, owner, balance=1000000.00):
        self.owner = owner
        self.balance = balance
        self.savings_rate = 0.07  # 7% interest

    def check_balance(self):
        print(f"\n{'='*40}\nAccount Owner: {self.owner}")
        print(f"Current Balance: ${self.balance:,.2f}\n{'='*40}")

    def calculate_savings(self):
        print("\n--- Savings Interest Calculator ---")
        try:
            years = int(input("Enter number of years to compound: "))
            if years < 0:
                print("Years cannot be negative!")
                return
            
            future_balance = self.balance * ((1 + self.savings_rate) ** years)
            interest = future_balance - self.balance
            
            print(f"\nProjections at {self.savings_rate*100}% annual interest:")
            print(f" • Total Interest Earned: ${interest:,.2f}")
            print(f" • Projected Balance: ${future_balance:,.2f}")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    def invest_options(self):
        print(f"\n--- Investment Marketplace ---\nAvailable Balance: ${self.balance:,.2f}")
        options = {
            "1": (0.10, "High-Yield Stocks"),
            "2": (0.07, "Real Estate Trust"),
            "3": (0.30, "Cryptocurrency")
        }
        
        for key, (rate, name) in options.items():
            print(f"{key}. {name} (Est. Return: {rate*100}% / year)")
        print("4. Go Back to Main Menu")

        choice = input("\nSelect an option (1-4): ")
        if choice == '4' or choice not in options:
            return

        rate, asset_name = options[choice]
        
        try:
            amount = float(input(f"Enter amount to invest (Max ${self.balance:,.2f}): "))
            if amount <= 0 or amount > self.balance:
                print("Invalid investment amount or insufficient funds.")
                return

            years = int(input("How many years do you want to hold this investment? "))
            
            print(f"\nProcessing investment into {asset_name}...")
            time.sleep(1)

            final_value = amount * ((1 + rate) ** years)
            profit = final_value - amount

            print(f"\n--- {asset_name} Performance ---")
            print(f" • Initial Capital: ${amount:,.2f}")
            print(f" • Final Value after {years} years: ${final_value:,.2f}")
            print(f" • Net Profit/Loss: ${profit:,.2f}")

            sell = input("\nWould you like to sell and cash out? (yes/no): ").lower()
            if sell in ['yes', 'y']:
                # Deduct original amount and add final value
                self.balance = (self.balance - amount) + final_value
                print(f"Cashed out! Balance updated.")
            else:
                print(f"Investment kept. Unsold simulation assets do not persist.")
        except ValueError:
            print("Input Error. Please enter valid numbers.")

# --- Main Program ---
if __name__ == "__main__":
    print("Welcome to the Python Terminal Bank Simulator!")
    name = input("Please enter your name: ").strip()
    bank = BankSimulator(owner=name)

    menu = {"1": bank.check_balance, "2": bank.calculate_savings, "3": bank.invest_options}

    while True:
        print("\n--- MAIN MENU ---\n1. Check Balance\n2. Calculate Savings Interest\n3. Explore Investments\n4. Exit")
        choice = input("\nWhat would you like to do? (1-4): ")
        
        if choice == '4':
            print(f"\nThank you for banking with us, {bank.owner}!")
            break
        elif choice in menu:
            menu[choice]()
        else:
            print("Invalid option. Please choose 1-4.")
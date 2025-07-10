# Step 1: Define hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320,
    "AMZN": 120
}

# Step 2: Get user input
portfolio = {}
print("📈 Enter your stock holdings. Type 'done' to finish.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            raise ValueError
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid positive integer.\n")

# Step 3: Calculate total investment
total_value = 0
print("\n🧾 Your Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Step 4 (Optional): Save to a .txt file
save = input("\nWould you like to save this report to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print("📁 Report saved to 'portfolio_report.txt'")

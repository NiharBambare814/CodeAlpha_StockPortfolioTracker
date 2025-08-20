# Hardcoded stock prices
stock_prices = {
    "TATA": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "ADOBE": 130
}

portfolio = {}
total_investment = 0

print("---- Stock Portfolio Tracker ----")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += quantity * stock_prices[stock]

print("\n---- Portfolio Summary ----")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    print(f"{stock}: {qty} shares @ {stock_prices[stock]} = ${value}")

print(f"Total Investment: ${total_investment}")

# Optional: Save to file
with open("portfolio_summary.txt", "w") as f:
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares @ {stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
    f.write(f"\nTotal Investment: ${total_investment}")

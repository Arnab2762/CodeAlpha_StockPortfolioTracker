# CodeAlpha Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

while True:

    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from:")
        print(", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(f"{stock} Price: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Investment: ${investment}")

print("\n===================================")
print(f"Total Investment: ${total_investment}")
print("===================================")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("========================\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("\nResult saved to portfolio.txt")
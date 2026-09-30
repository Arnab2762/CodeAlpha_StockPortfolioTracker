# CodeAlpha Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

# Every purchase the user enters is stored here
portfolio = []
total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from:")
        print(", ".join(stock_prices.keys()))
        continue

    # Validate quantity so a typo doesn't crash the program
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a whole number greater than 0.")
        continue

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    # Save all the details of this purchase
    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": price,
        "investment": investment,
    })

    print(f"{stock} Price: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Investment: ${investment}")

print("\n===================================")
print(f"Total Investment: ${total_investment}")
print("===================================")

# Save all details to a text file
if portfolio:
    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 48 + "\n")
        file.write(f"{'Stock':<8}{'Qty':>6}{'Price':>12}{'Investment':>16}\n")
        file.write("-" * 48 + "\n")
        for item in portfolio:
            file.write(
                f"{item['stock']:<8}{item['quantity']:>6}"
                f"{'$' + str(item['price']):>12}"
                f"{'$' + str(item['investment']):>16}\n"
            )
        file.write("=" * 48 + "\n")
        file.write(f"Total Stocks Purchased: {sum(i['quantity'] for i in portfolio)}\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("\nResult saved to portfolio.txt")
else:
    print("\nNo stocks entered, nothing saved.")
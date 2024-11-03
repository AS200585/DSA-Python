stock_prices = []

with open("sample_stock_price.csv", "r") as f:
    # Skip the header
    next(f)
    day = 1  # Initialize day counter or get it from the CSV if applicable
    for line in f:
        tokens = line.strip().split(',')
        try:
            price = float(tokens[1])  # Convert the second column to a float
            supplier = tokens[0]  # Define the variable supplier
            supplier_code = tokens[2]  # Define the variable supplier_code
            price_per = tokens[3]  # Define the variable price_per
            minimum_level = tokens[4]  # Define the variable minimum_level
            package_quantity = tokens[5]  # Define the variable package_quantity
            stock_prices.append([supplier, supplier_code, price_per, minimum_level, package_quantity])  # Append day and price to the list
            day += 1  # Increment day counter
        except ValueError:
            print(f"Skipping non-numeric value: {tokens[1]}")
# Print the stock_prices list
print(stock_prices)
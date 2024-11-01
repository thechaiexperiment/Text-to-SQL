few_shot_examples = [
    ("What is the total sales for 2022?", "SELECT SUM(sales) FROM sales_data WHERE year = 2022;"),
    ("List all customers from New York.", "SELECT * FROM customers WHERE city = 'New York';"),
    ("How many products were sold in January?", "SELECT SUM(quantity) FROM sales WHERE month = 'January';"),
    # Add more examples as necessary
]

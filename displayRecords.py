# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

import sqlite3

def getRecordsPerRow():
    while True:
        try:
            records_per_row = int(input("Enter the number of records to display per row: "))
            if records_per_row > 0:
                return records_per_row
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

            
def displayRecords(records_per_row, index=0):
    connection = sqlite3.connect('product.db')
    c = connection.cursor()
    c.execute("SELECT COUNT(*) FROM products")
    count_result = c.fetchone()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    
    if count_result[0] == 0:
        print("\N{Face Screaming in Fear} There are currently no products in the system!\n")

    #
    elif index < len(products):
        # Fetch the current row of products to display
        row_products = products[index:index + records_per_row]
        
        # Format each product in the row
        formatted_products = []
        for product in row_products:
            col_width = 50
            id, name, category, brand, supplier_since, stock = product
            id_gap = " " * (col_width - len(id) - 9)
            name_gap = " " * (col_width - len(name) - 11)
            category_gap = " " * (col_width - len(category) - 10)
            brand_gap = " " * (col_width - len(brand) - 7)
            supplier_since_gap = " " * (col_width - len(str(supplier_since)) - 16)
            stock_gap = " " * (col_width - len(stock) - 8)

            formatted_product = (
                f"Prod id: {id}{id_gap}\n"
                f"Prod Name: {name}{name_gap}\n"
                f"Category: {category}{category_gap}\n"
                f"Brand: {brand}{brand_gap}\n"
                f"Supplier Since: {supplier_since}{supplier_since_gap}\n"
                f"Stocks: {stock}{stock_gap}\n"
            )
            formatted_products.append(formatted_product)

        # Print the formatted products in a single row
        for line in zip(*[prod.split('\n') for prod in formatted_products]):
            print("    ".join(line))
        
        print()  # New line after each row for spacing
        
        # Recursively call the function for the next set of products
        displayRecords(records_per_row, index + records_per_row)

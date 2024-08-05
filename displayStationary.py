# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

import sqlite3
def displayStationary():
    connection = sqlite3.connect('product.db')
    c = connection.cursor()
    c.execute("SELECT COUNT(*) FROM products")
    count_result = c.fetchone()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    if count_result[0] == 0:
        print("\N{Face Screaming in Fear} There are currently no products in the system!\n")
    else:
        count = 1
        print("---------------------------------------------------------------------------")
        print("products List: ")
        for row in products:
            id, name, category, brand, supplier_since, stock = row
            print(f"Product ID: {id}")
            print(f"Product Name: {name}")
            print(f"Product Category: {category}")
            print(f"Brand: {brand}")
            print(f"Supplier Year: {supplier_since}")
            print(f"Stock: {stock}")
            print("---------------------------------------------------------------------------")
            count += 1
    
    connection.commit()
    connection.close()
            
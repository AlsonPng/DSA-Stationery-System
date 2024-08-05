import sqlite3

def selectionSort():
    connection = sqlite3.connect('product.db')
    c = connection.cursor()
    c.execute("SELECT * FROM products")
    prodList = c.fetchall()

    if not prodList:
        print("There are currently no products in the system!\n")
        return

    n = len(prodList)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if prodList[j][0] > prodList[max_idx][0]:  # Sorting by Prod_id (index 0)
                max_idx = j
        prodList[i], prodList[max_idx] = prodList[max_idx], prodList[i]
        print(f"Pass {i + 1}: {[item[0] for item in prodList]}")

    # Update the database with the sorted list
    c.execute("DELETE FROM products")
    c.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", prodList)
    connection.commit()
    connection.close()

    print("Products have been sorted by Prod_id in descending order.")
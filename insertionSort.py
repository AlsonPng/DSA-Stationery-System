# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

from displayStationary import displayStationary
import sqlite3
def insertionSort(prodList):
    if prodList == []:
        print("\N{Face Screaming in Fear} There are currently no products in the system!\n")
        return prodList
    
    print
    for i in range(1, len(prodList)):
        current_item = prodList[i]
        j = i - 1
        print(f"Pass {i+1}:")
        print("---------------------------------------------------------------------------")
        while j >= 0 and prodList[j][3] > current_item[3]:
            prodList[j + 1] = prodList[j]
            j -= 1
        for k in range(0, len(prodList)):
            print(f"{prodList[k][0]}")
        prodList[j + 1] = current_item
        print("---------------------------------------------------------------------------")

    connection = sqlite3.connect('product.db')
    c = connection.cursor()
    c.execute("DELETE FROM products")
    insert = "INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)"
    for i in prodList:
        c.execute(insert, i)
    connection.commit()
    connection.close()
    display = input("Do you want to display the sorted list (Y/N)? ").lower()
    if display == "y":
        displayStationary()
    else:
        print()

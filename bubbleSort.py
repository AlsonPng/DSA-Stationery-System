# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

from displayRecords import displayRecords
import sqlite3
def bubbleSort(prodList, records_per_row):
    if prodList == []:
        print("\N{Face Screaming in Fear} There are currently no products in the system!\n")
        return prodList

    for i in range(len(prodList) - 1):
        swapped = False
        print(f"Pass {i+1}:\n")
        print("---------------------------------------------------------------------------")
        for j in range(len(prodList) - i - 1):
            if prodList[j][2] < prodList[j + 1][2]:
                prodList[j], prodList[j + 1] = prodList[j + 1], prodList[j]
                swapped = True
        for k in range(0, len(prodList)):
            print(f"{prodList[k][0]}")
        print("---------------------------------------------------------------------------")
        if not swapped:
            break

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
        displayRecords(records_per_row)
    else:
        print()

# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

import sqlite3
from displayRecords import displayRecords

def mergeSort(stationary_list):
    if len(stationary_list) > 1:
        mid = len(stationary_list) // 2
        left_half = stationary_list[:mid]
        right_half = stationary_list[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][2] < right_half[j][2]:  # Sorting by Category (index 2)
                stationary_list[k] = left_half[i]
                i += 1
            elif left_half[i][2] == right_half[j][2] and left_half[i][4] < right_half[j][4]:  # Then by Stock (index 4)
                stationary_list[k] = left_half[i]
                i += 1
            else:
                stationary_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            stationary_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            stationary_list[k] = right_half[j]
            j += 1
            k += 1

        dashStr = "-" * 30
        prod_ids = "\n".join([f"Prod_id: {item[0]}" for item in stationary_list])
        print(f"New List: \n{dashStr}\n{prod_ids}\n{dashStr}")

def performMergeSort(records_per_row):
    connection = sqlite3.connect('product.db')
    c = connection.cursor()
    c.execute("SELECT * FROM products")
    prodList = c.fetchall()

    if not prodList:
        print("There are currently no products in the system!\n")
        return

    mergeSort(prodList)
    displayRecords(records_per_row)

    # Update the database with the sorted list
    c.execute("DELETE FROM products")
    c.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", prodList)
    connection.commit()
    connection.close()


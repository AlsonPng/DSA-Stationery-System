from RestockDetail import RestockDetail
import sqlite3
from handleNextDelivery import handleNextDelivery

def restocking(restockingQ):
    conn = sqlite3.connect('product.db')
    c = conn.cursor()

    # Fetch all existing product IDs
    c.execute('SELECT id FROM products')
    existing_product_ids = {row[0] for row in c.fetchall()}

    while True:
        prod_id = input("Enter a valid existing product ID: ")
        if prod_id in existing_product_ids:
            quantity = int(input("Enter the quantity to restock: "))
            restockingQ.enqueue(RestockDetail(prod_id, quantity))
            break
        else:
            print("Invalid product ID. Please try again.")

    conn.close()
    return restockingQ

def restockingMenu(restockingQ):
    while True:
        print("\nRestocking Menu:")
        print("1. Enter new stock arrival")
        print("2. View Number of stock arrival")
        print("3. Service next restock in queue")
        print("0. Return to Main Menu")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                restocking(restockingQ=restockingQ)
            case "2":
                print("Number of stock arrival:", restockingQ.__len__())
            case "3":
                handleNextDelivery(restockingQ)
            case "0":
                break
            case _:
                print("Invalid choice. Please try again.")
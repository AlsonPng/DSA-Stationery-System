# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

import sqlite3
from colorama import Fore
from pyfiglet import figlet_format
from populateData import populateData
from displayStationary import displayStationary
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from addStationary import addStationary
from selectionSort import selectionSort
from mergeSort import performMergeSort
from restocking import restockingMenu
from displayRecords import displayRecords, getRecordsPerRow
from Queue import RestockingQ as Queue

global restockingQ 
restockingQ = Queue()
global records_per_row
records_per_row = 1

def initializeDatabase():
    connection = sqlite3.connect('product.db')
    c = connection.cursor()
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS products (
                            id TEXT PRIMARY KEY,
                            name TEXT,
                            category TEXT,
                            brand TEXT,
                            supplier_since DATE,
                            stock TEXT
                        )''')
    except sqlite3.OperationalError as e:
        print("Error creating table:", e)
    connection.commit()
    connection.close()

def main():
    initializeDatabase()
    print(Fore.LIGHTBLUE_EX, figlet_format("Stationary Management System", font = "speed"), Fore.WHITE)
    viewMenu()

def viewMenu():
    global records_per_row
    print("1. Add a new Stationary. ")
    print("2. Display all Stationary. ")
    print("3. Sort Stationary via Bubble sort on Category. ")
    print("4. Sort Stationary via Insertion sort on Brand ")
    print("5. Sort Stationary via Selection sort on Prod id ")
    print("6. Sort Stationary via Merge sort on Category follow by stock in ascending order ")
    print("7. Go to Restocking Menu ")
    print("8. Set number of records per row to display ") 
    print("9. Populate data. ")
    print("0. Exit program. ")
    menuChoice = input(f"Please select one {Fore.MAGENTA}(1,2,3,4,5,6,7,8,9 or 0){Fore.WHITE}: ")
    running = True

    while running:
        prodList = []
        connection = sqlite3.connect('product.db')
        c = connection.cursor()
        # c.execute("DELETE FROM products")
        c.execute("SELECT * from products")

        products = c.fetchall()
        prodList = products
        connection.commit()
        connection.close()
        match menuChoice:
            case "1":
                addStationary(prodList)
                return(viewMenu())
            case "2":
                displayRecords(records_per_row)
                return (viewMenu())
            case "3":
                bubbleSort(prodList, records_per_row=records_per_row)
                return(viewMenu())
            case "4":
                insertionSort(prodList, records_per_row=records_per_row)
                return(viewMenu())
            case "5":
                selectionSort(records_per_row=records_per_row)
                return(viewMenu())
            case "6":
                performMergeSort(records_per_row=records_per_row)
                return(viewMenu())
            case "7":
                restockingMenu(restockingQ)
                return(viewMenu())
            case "8":
                records_per_row = getRecordsPerRow()
                displayRecords(records_per_row)
                return(viewMenu())
            case "9":
                populateData(prodList)
                return(viewMenu())
            case "0":
                print("\N{Door}\N{Pedestrian} Exiting The Program. \n")
                running = False
                exit()
            case _:
                print("\N{Face Screaming in Fear} Invalid option please try again.\n")
                viewMenu()

if __name__ == "__main__":
    main()
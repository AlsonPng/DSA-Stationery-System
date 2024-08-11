# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

import sqlite3
from datetime import date
from Stationary import Stationary
def addStationary(prodList):
        while True:
            inputId = input("\nEnter id: ")
            inputId_temp = inputId.replace(" ", "")
            if not inputId_temp.strip():
                print("Product ID cannot be empty. Please try again.")
            elif not inputId_temp.isalnum():
                print("Product ID can only contain letters and numbers. Please try again.")
            else:
                is_unique = True  # Flag to track uniqueness
                connection = sqlite3.connect('product.db')
                c = connection.cursor()
                c.execute("SELECT * FROM products")
                products = c.fetchall()
                for row in products:
                    id, name, category, brand, supplier_since, stock = row
                    if id.lower() == inputId.lower():
                        print("Product ID must be unique. Please try again. ")
                        is_unique = False 
                        connection.close
                        break
                if is_unique:
                    break


        while True:
            name = input("Enter name: ")
            name_temp = name.replace(" ", "")
            if not name_temp.strip():
                print("Name cannot be empty. Please try again.")
            elif not name_temp.isalnum():
                print("Name can only contain letters and numbers. Please try again.")
            else:
                break

        while True:
            category = input("Enter category: ")
            category_temp = category.replace(" ", "")
            if not category_temp.strip():
                print("Category cannot be empty. Please try again.")
            elif not category_temp.isalpha():
                print("Category can only contain letters. Please try again.")
            else:
                break

        while True:
            brand = input("Enter brand: ")
            brand_temp = brand.replace(" ", "")
            if not brand_temp.strip():
                print("Brand cannot be empty. Please try again.")
            elif not brand_temp.isalpha():
                print("Brand can only contain letters. Please try again.")
            else:
                break

        while True:
            supplier_since = input("Enter supplier since year ____: ")
            supplier_since_temp = supplier_since.replace(" ", "")
            if not supplier_since_temp.strip():
                print("Supplier since year cannot be empty. Please try again.")
            elif not supplier_since_temp.isnumeric():
                print("Supplier since year can only contain numbers. Please try again.")
            else:
                year = int(supplier_since)
                if len(supplier_since) != 4 or year > date.today().year:
                    print("Please enter a valid year.")
                else:
                    supplier_since = year
                    break  # Exit the loop after successful validation and assignment

        while True:
            stock = input("Stock quantity: ")
            stock_temp = stock.replace(" ", "")
            if not stock_temp.strip():
                print("Stock quantity cannot be empty. Please try again.")
            elif not stock_temp.isnumeric():
                print("Stock quantity can only contain numbers. Please try again.")
            else:
                break

        
        stationary = Stationary(inputId, name, category, brand, supplier_since, stock)
        connection = sqlite3.connect('product.db')
        c = connection.cursor()
        sql = "INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)"
        id = stationary.getId()
        name = stationary.getName()
        category = stationary.getCategory()
        brand = stationary.getBrand()
        supplier_since = stationary.getSupplierSince()
        stock = stationary.getStock()
        c.execute(sql, (id, name, category, brand, supplier_since, stock))
        # c.execute("SELECT * from products")
        # products = c.fetchall()
        # prodList = []
        # print(prodList)
        # for row in products:
        #     id, name, category, brand, supplier_since = row
        #     prodList.append(row)
        c.execute("SELECT * from products")
        products = c.fetchall()
        prodList = products
        connection.commit()
        connection.close()
        print("Stationary added!\n")
        return prodList
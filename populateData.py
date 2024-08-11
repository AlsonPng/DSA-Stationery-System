# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

import Stationary
import sqlite3
def populateData(prodList):

    tempList = []
    newStudA = Stationary.Stationary("PD1020", "Pastel Art Paper", "Paper", "Faber-Castell", 2021, 2000)
    newStud = (newStudA.getId(), newStudA.getName(), newStudA.getCategory(), newStudA.getBrand(), newStudA.getSupplierSince(), newStudA.getStock())
    if newStud in prodList:
        print("Data already populated!\n")
        return prodList
    prodList.append(newStud)
    tempList.append(newStud)
    newStudA = Stationary.Stationary("PD1025", "Mars Lumograph Drawing Pencils", "Pencils", "Staedtler", 2022, 320)
    newStud = (newStudA.getId(), newStudA.getName(), newStudA.getCategory(), newStudA.getBrand(), newStudA.getSupplierSince(), newStudA.getStock())
    prodList.append(newStud)
    tempList.append(newStud)
    newStudA = Stationary.Stationary("PD1015", "Water color Pencils", "Pencils", "Faber-Castell", 2011, 150)
    newStud = (newStudA.getId(), newStudA.getName(), newStudA.getCategory(), newStudA.getBrand(), newStudA.getSupplierSince(), newStudA.getStock())
    prodList.append(newStud)
    tempList.append(newStud)
    newStudA = Stationary.Stationary("PD1050", "Noris 320 fiber tip pen", "Pens", "Staedtler", 2021, 350)
    newStud = (newStudA.getId(), newStudA.getName(), newStudA.getCategory(), newStudA.getBrand(), newStudA.getSupplierSince(), newStudA.getStock())
    prodList.append(newStud)
    tempList.append(newStud)
    newStudA = Stationary.Stationary("PD1001", "Copier Paper (A4) 70GSM", "Paper", "PaperOne", 2021, 1500)
    newStud = (newStudA.getId(), newStudA.getName(), newStudA.getCategory(), newStudA.getBrand(), newStudA.getSupplierSince(), newStudA.getStock())
    prodList.append(newStud)
    tempList.append(newStud)
    newStudA = Stationary.Stationary("PD1033", "Scientific Calculator FX-97SG X", "Calculator", "Casio", 2022, 50)
    newStud = (newStudA.getId(), newStudA.getName(), newStudA.getCategory(), newStudA.getBrand(), newStudA.getSupplierSince(), newStudA.getStock())
    prodList.append(newStud)
    tempList.append(newStud)
    newStudA = Stationary.Stationary("PD1005", "POP Bazic File Separator Clear", "Office Supplies", "Popular", 2000, 500)
    newStud = (newStudA.getId(), newStudA.getName(), newStudA.getCategory(), newStudA.getBrand(), newStudA.getSupplierSince(), newStudA.getStock())
    prodList.append(newStud)
    tempList.append(newStud)
    connection = sqlite3.connect('product.db')
    c = connection.cursor()
    insert = "INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)"
    for item in tempList:
        c.execute(insert, item)
    connection.commit()
    connection.close
    print("Data populated!\n")
    return prodList

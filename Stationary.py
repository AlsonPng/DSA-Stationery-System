# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

class Stationary:
    def __init__(self, id, name, category, brand, supplier_since, stock):
        self.__id = id
        self.__name = name
        self.__category = category
        self.__brand = brand
        self.__supplier_since = supplier_since
        self.__stock = stock

    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getCategory(self):
        return self.__category
    def getBrand(self):
        return self.__brand
    def getSupplierSince(self):
        return self.__supplier_since
    def getStock(self):
        return self.__stock
    
    def setId(self, id):
        self.__id = id
    def setName(self, name):
        self.__name = name
    def setCategory(self, category):
        self.__category = category
    def setBrand(self, brand):
        self.__brand = brand
    def setSupplierSince(self, supplier_since):
        self.__supplier_since = supplier_since
    def setStock(self, stock):
        self.__stock = stock

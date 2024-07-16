# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5


from typing import Any
class Stationary:
    def __init__(self, id, name, category, brand, supplier_since):
        self.__id = id
        self.__name = name
        self.__category = category
        self.__brand = brand
        self.__supplier_since = supplier_since

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
    
    def setId(self):
        return self.__id
    def setName(self):
        return self.__name
    def setCategory(self):
        return self.__category
    def setBrand(self):
        return self.__brand
    def setSupplierSince(self):
        return self.__supplier_since

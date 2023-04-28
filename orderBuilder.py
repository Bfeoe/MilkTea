from foodType import *
from foodFactory import *

class order:
    beverage = None
    price = 0.0
    order_id = 0

    def __init__(self, orderBuilder):
        self.beverage = orderBuilder.bBeverage

    def __str__(self):
        return f"order{self.order_id}: {self.beverage.getName()} {self.beverage.getCup()} {self.beverage.getHeat()}"

    def setOrder_id(self, xOrder_id):
        self.order_id = xOrder_id

    def show(self):
        print("Order:")
        print("name:", self.beverage.getName())
        print("Heat: ", self.beverage.getHeat())
        print("Cup:", self.beverage.getCup())
        print("Sugar:", self.beverage.getSugar())


class OrderBuilder:

    bBeverage = ""
    def __init__(self):
        self.bBeverage = Beverage()
    def setBeverage(self, xBeverage):
        beverage_factory = foodFactory()
        self.bBeverage = beverage_factory.make(xBeverage)

    def setHeat(self, xHeat):
        self.bBeverage.setHeat(xHeat)

    def setCup(self, xCup):
        self.bBeverage.setCup(xCup)

    def setSugar(self, xSugar):
        self.bBeverage.setSugar(xSugar)

    def build(self):
        return order(self)


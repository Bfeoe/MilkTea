from abstract_factory import *


class Order:
    beverage = ""

    def __init__(self, orderBuilder):
        self.beverage = orderBuilder.bBeverage

    def show(self):0n
        print("name:%s " % self.beverage.getName())
        print("heat:%s " % self.beverage.heat)
        print("cup:%s " % self.beverage.cup)


class OrderBuilder:
    bBeverage = ""

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def addHeat(self, xHeat):
        self.bBeverage.heat = xHeat

    def addCup(self, xCup):
        self.bBeverage.cup = xCup

    def build(self):
        return Order(self)

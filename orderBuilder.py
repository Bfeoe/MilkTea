from foodType import *


class order:
    beverage = ""

    def __init__(self, orderBuilder):
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print("Beverage:%s" % self.beverage.getName())
        print("Heat:%s " % self.beverage.getHeat())
        print("Cup:%s " % self.beverage.getCup())


class OrderBuilder:
    bBeverage = ""

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def addHeat(self, xHeat):
        self.bBeverage.heat = xHeat

    def addCup(self, xCup):
        self.bBeverage.cup = xCup

    def build(self):
        return order(self)


if __name__ == "__main__":
    order_builder = OrderBuilder()
    order_builder.addBeverage(MochaCoffee())
    order_1 = order_builder.build()
    order_1.show()

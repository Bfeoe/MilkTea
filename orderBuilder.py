from foodType import *


class order:
    beverage = None

    def __init__(self, orderBuilder):
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print("Beverage:", self.beverage.getName())
        print("Heat: ", self.beverage.getHeat())
        print("Cup:", self.beverage.getCup())


class OrderBuilder:
    bBeverage = ""

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def addHeat(self, xHeat):
        self.bBeverage.setHeat(xHeat)

    def addCup(self, xCup):
        self.bBeverage.setCup(xCup)

    def build(self):
        return order(self)


if __name__ == "__main__":
    order_builder = OrderBuilder()
    order_builder.addBeverage(GrapeCustard())
    order_builder.addCup("大杯")
    order_builder.addHeat("热")
    order_1 = order_builder.build()
    order_1.show()

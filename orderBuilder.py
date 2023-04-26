from foodType import *


class order:
    beverage = None

    def __init__(self, orderBuilder):
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print("Order:")
        print("name:", self.beverage.getName())
        print("Heat: ", self.beverage.getHeat())
        print("Cup:", self.beverage.getCup())


class OrderBuilder:
    bBeverage = ""

    def setBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def setHeat(self, xHeat):
        self.bBeverage.setHeat(xHeat)

    def setCup(self, xCup):
        self.bBeverage.setCup(xCup)

    def build(self):
        return order(self)


if __name__ == "__main__":
    order_builder = OrderBuilder()
    order_builder.setBeverage(GrapeCustard())
    order_builder.setCup("大杯")
    order_builder.setHeat("热")
    order_1 = order_builder.build()
    order_1.show()

from abc import abstractmethod, ABCMeta
from orderBuilder import *
from warehouse import *
from foodType import *


class WaiterSys:
    orderList = []

    def addOrder(self, xOrder):
        print("WAITER: Add order...")
        self.orderList.append(xOrder)

    def removeOrder(self, xOrder):
        print("WAITER: Cancel order...")
        self.orderList.remove(xOrder)

    def cookBeverage(self):
        print("WAITER: Making beverage...")
        for Order in self.orderList:
            beverage_sys = MakeCommand(Order)
            beverage_sys.cook()


class Command(metaclass=ABCMeta):
    beverage = ""
    portion = 0

    def __init__(self, xBeverage):
        self.beverage = xBeverage
        if self.beverage.cup == "小杯":
            self.portion = 1
        else:
            self.portion = 2

    def decrease(self):
        for material in self.beverage.material:
            if MilkWarehouse.goods.get(material):
                if MilkWarehouse.goods[material] - self.portion * 350 < 0:
                    print(f"{material}不足，无法制作")
                else:
                    print(f"putting {self.portion * 350}ml {material}")
                    MilkWarehouse.goods[material] -= self.portion * 350

            elif TeaWarehouse.goods.get(material):
                if TeaWarehouse.goods[material] - self.portion * 350 < 0:
                    print(f"{material}不足，无法制作")
                else:
                    print(f"putting {self.portion * 350}ml {material}")
                    TeaWarehouse.goods[material] -= self.portion * 350
            elif FruitWarehouse.goods.get(material):
                if FruitWarehouse.goods[material] - self.portion * 1 < 0:
                    print(f"{material}不足，无法制作")
                else:
                    print(f"cutting {self.portion * 150}g {material}")
                    FruitWarehouse.goods[material] -= self.portion * 1
            elif IngredientWarehouse.goods.get(material):
                if IngredientWarehouse.goods[material] - self.portion * 1 < 0:
                    print(f"{material}不足，无法制作")
                else:
                    print(f"putting {self.portion * 50}g {material}")
                    IngredientWarehouse.goods[material] -= self.portion * 1

    @abstractmethod
    def cook(self):
        pass


def MakeCommand(Order):
    if Order.beverage.type == "MILKTEA":
        return MilkTeaSys(Order.beverage)
    elif Order.beverage.type == "TEA":
        return TeaSys(Order.beverage)
    elif Order.beverage.type == "JUICE":
        return JuiceSys(Order.beverage)
    elif Order.beverage.type == "FRUIT-TEA":
        return FruitTeaSys(Order.beverage)
    elif Order.beverage.type == "COFFEE":
        return CoffeeSys(Order.beverage)
    elif Order.beverage.type == "SMOOTHIE":
        return SmoothieSys(Order.beverage)
    else:
        print("Something wring")
        return False


class MilkTeaSys(Command):
    def cook(self):
        print(f"{self.beverage.getName()}制作中...")
        self.decrease()
        print("mixing well")
        return self.beverage


class JuiceSys(Command):
    def cook(self):
        print(f"{self.beverage.getName()}制作中...")
        self.decrease()
        print("putting fruit into juice extractor")
        print("juicing")
        return self.beverage


class FruitTeaSys(Command):
    def cook(self):
        print(f"{self.beverage.getName()}制作中...")
        self.decrease()
        print("putting fruit into tea")
        print("mixing well")
        return self.beverage


class TeaSys(Command):
    def cook(self):
        print(f"{self.beverage.getName()}制作中...")
        self.decrease()
        return self.beverage


class CoffeeSys(Command):
    def cook(self):
        print(f"{self.beverage.getName()}制作中...")
        print("take some coffee bean")
        print("grounding coffee")
        print("making coffee")
        self.decrease()
        return self.beverage


class SmoothieSys(Command):
    def cook(self):
        print(f"{self.beverage.getName()}制作中...")
        self.decrease()
        print("shaving ice")
        return self.beverage


if __name__ == "__main__":
    order_builder = OrderBuilder()
    order = []
    order_builder.setBeverage(OreoMilkTea())
    order_builder.setCup("大杯")
    order_builder.setHeat("热")
    order.append(order_builder.build())
    order_builder.setBeverage(LemonJuice())
    order_builder.setCup("大杯")
    order_builder.setHeat("冷")
    order.append(order_builder.build())
    order_builder.setBeverage(HoneyGrapefruitTea())
    order_builder.setCup("大杯")
    order_builder.setHeat("冷")
    order.append(order_builder.build())
    order_builder.setBeverage(ABucketOfFruitTea())
    order_builder.setCup("小杯")
    order_builder.setHeat("冷")
    order.append(order_builder.build())
    order_builder.setBeverage(IceCreamCoffee())
    order_builder.setCup("小杯")
    order.append(order_builder.build())
    order_builder.setBeverage(PeachSmoothie())
    waiter = WaiterSys()
    for orders in order:
        waiter.addOrder(orders)
    waiter.cookBeverage()


from abc import abstractmethod, ABCMeta
from orderBuilder import *
from warehouse import *
from foodType import *


class WaiterSys:
    orderList = []
    product = []

    def addOrder(self, xOrder):
        self.orderList.append(xOrder)
        xOrder.setOrder_id(self.orderList.index(xOrder)+1)
        print("WAITER: Add", xOrder)

    def removeOrder(self, xOrder_id):
        print(f"WAITER: order{xOrder_id+1}已取消")
        self.orderList[xOrder_id] = None

    def cookBeverage(self):
        print("WAITER: Making beverage...")
        for order_id in range(len(self.orderList)):
            beverage_sys = MakeCommand(self.orderList[order_id])
            self.product.append(beverage_sys.cook())
            if self.product[order_id]:
                print(self.orderList[order_id])
                print("已制作完成, 收费：", self.product[order_id].price)
            else:
                print(self.orderList[order_id], "-材料不足，无法制作")
                self.removeOrder(order_id)


class Command(metaclass=ABCMeta):
    beverage = ""
    portion = 0
    MF = 4.0
    cost = 0.0
    state = None

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
                    print(f"  {material}不足，无法制作")
                    return False
                else:
                    print(f"  putting {self.portion * 150}ml {material}")
                    MilkWarehouse.goods[material] -= self.portion * 350
            elif TeaWarehouse.goods.get(material):
                if TeaWarehouse.goods[material] - self.portion * 350 < 0:
                    print(f"  {material}不足，无法制作")
                    return False
                else:
                    print(f"  putting {self.portion * 150}ml {material}")
                    TeaWarehouse.goods[material] -= self.portion * 350
            elif FruitWarehouse.goods.get(material):
                if FruitWarehouse.goods[material] - self.portion * 1 < 0:
                    print(f"  {material}不足，无法制作")
                    return False
                else:
                    print(f"  cutting {self.portion * 150}g {material}")
                    FruitWarehouse.goods[material] -= self.portion * 1
            elif IngredientWarehouse.goods.get(material):
                if IngredientWarehouse.goods[material] - self.portion * 1 < 0:
                    print(f"  {material}不足，无法制作")
                    return False
                else:
                    print(f"  putting {self.portion * 50}g {material}")
                    IngredientWarehouse.goods[material] -= self.portion * 1
        return True

    @abstractmethod
    def cook(self):
        pass
    def setPrice(self):
        for material in self.beverage.material:
            if MilkWarehouse.goods.get(material):
                self.cost += MilkWarehouse.unit_price[material]
            elif TeaWarehouse.goods.get(material):
                self.cost += TeaWarehouse.unit_price[material]
            elif FruitWarehouse.goods.get(material):
                self.cost += FruitWarehouse.unit_price[material]
            elif IngredientWarehouse.goods.get(material):
                self.cost += IngredientWarehouse.unit_price[material]
        if self.portion == 1:
            self.beverage.price = self.cost + self.MF
        else:
            self.beverage.price = 2 * self.cost + self.MF


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
        print(f"  {self.beverage.getName()}制作中...")
        self.state = self.decrease()
        if self.state:
            self.setPrice()
        else:
            return False
        print("  mixing well")
        return self.beverage


class JuiceSys(Command):
    def cook(self):
        print(f"  {self.beverage.getName()}制作中...")
        self.state = self.decrease()
        if self.state:
            self.setPrice()
        else:
            return False
        print("  putting fruit into juice extractor")
        print("  juicing")
        return self.beverage


class FruitTeaSys(Command):
    def cook(self):
        print(f"  {self.beverage.getName()}制作中...")
        self.state = self.decrease()
        if self.state:
            self.setPrice()
        else:
            return False
        print("  putting fruit into tea")
        print("  mixing well")
        return self.beverage


class TeaSys(Command):
    def cook(self):
        print(f"  {self.beverage.getName()}制作中...")
        self.state = self.decrease()
        if self.state:
            self.setPrice()
        else:
            return False
        return self.beverage


class CoffeeSys(Command):
    def cook(self):
        print(f"  {self.beverage.getName()}制作中...")
        print("  take some coffee bean")
        print("  grounding coffee")
        print("  making coffee")
        self.state = self.decrease()
        if self.state:
            self.setPrice()
        else:
            return False
        return self.beverage


class SmoothieSys(Command):
    def cook(self):
        print(f"  {self.beverage.getName()}制作中...")
        self.state = self.decrease()
        if self.state:
            self.setPrice()
        else:
            return False
        print("  shaving ice")
        return self.beverage


if __name__ == "__main__":
    order_builder = OrderBuilder()
    order = []
    order_builder.setBeverage(OreoMilkTea())
    order_builder.setCup("大杯")
    order_builder.setHeat("热")
    order.append(order_builder.build())
    order_builder.setBeverage(OreoMilkTea())
    order_builder.setCup("大杯")
    order_builder.setHeat("冷")
    order.append(order_builder.build())
    order_builder.setBeverage(OreoMilkTea())
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
    order.append(order_builder.build())
    waiter = WaiterSys()
    for orders in order:
        waiter.addOrder(orders)
    waiter.cookBeverage()

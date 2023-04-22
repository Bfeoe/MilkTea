from abc import abstractmethod, ABCMeta


class Colleague:
    mediator = None

    def __init__(self, mediator):
        self.mediator = mediator


class PurchaseColleague(Colleague):
    def buyStuff(self, num):
        print("PURCHASE: Bought %s" % num)
        self.mediator.execute("buy", num)

    @staticmethod
    def getNotice(content):
        print("PURCHASE: Get Notice---%s" % content)


class WarehouseColleague(Colleague):
    total = 0
    threshold = 100

    def setThreshold(self, threshold):
        self.threshold = threshold

    def isEnough(self):
        if self.total < self.threshold:
            print("WAREHOUSE: Warning...Stock is low...")
            self.mediator.execute("warning", self.total)
            return False
        else:
            return True

    def inc(self, num):
        self.total += num
        print("WAREHOUSE: Increase %s" % num)
        self.mediator.execute("increase", num)
        self.isEnough()

    def dec(self, num):
        if num > self.total:
            print("WAREHOUSE: Error...Stock is not enough")
        else:
            self.total -= num
            print("WAREHOUSE: Decrease %s" % num)
            self.mediator.execute("decrease", num)
        self.isEnough()


class SalesColleague(Colleague):
    def sellStuff(self, num):
        print("SALES: Sell %s" % num)
        self.mediator.execute("sell", num)

    @staticmethod
    def getNotice(content):
        print("SALES: Get Notice---%s" % content)


class AbstractMediator(metaclass=ABCMeta):
    purchase = ""
    sales = ""
    warehouse = ""

    def setPurchase(self, purchase):
        self.purchase = purchase

    def setWarehouse(self, warehouse):
        self.warehouse = warehouse

    def setSales(self, sales):
        self.sales = sales

    @abstractmethod
    def execute(self, content, num):
        pass


class StockMediator(AbstractMediator):
    def execute(self, content, num):
        print("Mediator: Get Info-%s" % content)
        if content == "buy":
            self.warehouse.inc(num)
            self.sales.getNotice("Bought %s" % num)
        elif content == "increase":
            self.sales.getNotice("Inc %s" % num)
            self.purchase.getNotice("Inc %s" % num)
        elif content == "decrease":
            self.sales.getNotice("Dec %s" % num)
            self.purchase.getNotice("Dec %s" % num)
        elif content == "warning":
            self.sales.getNotice("Stock is low. %s left." % num)
            self.purchase.getNotice("Stock is low. Please buy more! %s left" % num)
        elif content == "sell":
            self.warehouse.dec(num)
            self.purchase.getNotice("Sold %s" % num)
        else:
            pass


if __name__ == "__main__":
    mobile_mediator = StockMediator()
    mobile_purchase = PurchaseColleague(mobile_mediator)
    mobile_warehouse = WarehouseColleague(mobile_mediator)
    mobile_sales = SalesColleague(mobile_mediator)
    mobile_mediator.setPurchase(mobile_purchase)
    mobile_mediator.setWarehouse(mobile_warehouse)
    mobile_mediator.setSales(mobile_sales)

    mobile_warehouse.setThreshold(200)
    mobile_purchase.buyStuff(300)
    mobile_sales.sellStuff(120)

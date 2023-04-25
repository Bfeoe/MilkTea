class drinkDecorator():
    def getName(self):
        pass

    def getPrice(self):
        pass


class iceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +正常冰"


class normalDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +常温"


class lessIceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +少冰"


class hotDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +热饮"


class noIceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +去冰"


class regularSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +正常糖"


class lessSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +七分糖"


class halfSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +半糖"


class lightSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +三分糖"


class noSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +无糖"


class mixDecorator(drinkDecorator):
    def __init__(self,beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +mix"

    def getPrice(self):
        return self.beverage.getPrice() + 1

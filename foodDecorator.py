
class drinkDecorator():
    def getName(self):
        pass
    def getPrice(self):
        pass
    def getCook(self):
        pass
    def delIngredient(self):
        pass


class iceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +正常冰"

    def getCook(self):
        return self.beverage.getCook() + " 正常加冰"


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

    def getCook(self):
        return self.beverage.getCook() + " 加少量冰"


class hotDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +热饮"

    def getCook(self):
        return self.beverage.getCook() + " 加热保温"


class noIceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +去冰"

    def getCook(self):
        return self.beverage.getCook() + " 正常加冰，然后将冰取出"


class regularSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +正常糖"

    def getCook(self):
        return self.beverage.getCook() + " 正常加糖"


class lessSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +七分糖"

    def getCook(self):
        return self.beverage.getCook() + " 加入七分糖"


class halfSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +半糖"

    def getCook(self):
        return self.beverage.getCook() + " 加入五分糖"


class lightSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +三分糖"

    def getCook(self):
        return self.beverage.getCook() + " 加入三分糖"


class noSugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +无糖"


class sagoDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加西米"

    def getPrice(self):
        return self.beverage.getPrice() + 1

    def getCook(self):
        return self.beverage.getCook() + " 在顶部加入西米"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class coconutDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加椰果"

    def getPrice(self):
        return self.beverage.getPrice() + 1

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入椰果"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class pearlDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加珍珠"

    def getPrice(self):
        return self.beverage.getPrice() + 1

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入珍珠"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class poiDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加芋泥"

    def getPrice(self):
        return self.beverage.getPrice() + 2

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入芋泥"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class taroCircleDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加芋圆"

    def getPrice(self):
        return self.beverage.getPrice() + 2

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入芋圆"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class custardDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加奶冻"

    def getPrice(self):
        return self.beverage.getPrice() + 2

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入奶冻"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class glutinousRiceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加糯米"

    def getPrice(self):
        return self.beverage.getPrice() + 2

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入糯米"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class oreoDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加奥利奥"

    def getPrice(self):
        return self.beverage.getPrice() + 2

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入奥利奥"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class sweetPotatoDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加麻薯"

    def getPrice(self):
        return self.beverage.getPrice() + 3

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入麻薯"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class milkCapDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加奶盖"

    def getPrice(self):
        return self.beverage.getPrice() + 3

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入奶盖"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1


class iceCreamDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +加冰激凌"

    def getPrice(self):
        return self.beverage.getPrice() + 6

    def getCook(self):
        return self.beverage.getCook() + " 在顶上加入冰激凌"

    def delIngredient(self):
        return self.beverage.delIngredint() - 1

if  __name__=="__main__":
    coke_cola=coke()
    print("Name:%s" % coke_cola.getName())
    print("Price:%s" % coke_cola.getPrice())
    ice_coke=iceDecorator(coke_cola)
    print("Name:%s" % ice_coke.getName())
    print("Price:%s" % ice_coke.getPrice())

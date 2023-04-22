from abc import abstractmethod, ABCMeta


class Beverage:
    name = ''
    price: float = 0.0
    type = ""
    heat = ''
    cup = ''

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

    def setHeat(self, heat):
        self.heat = heat

    def getHeat(self):
        return self.heat

    def setCup(self, cup):
        self.cup = cup

    def getCup(self):
        return self.cup


class Tea(Beverage):
    type = "TEA"

class BlackTea(Tea):
    def __init__(self):
        self.name = "Black tea"
class PuerTea(Tea):
    def __init__(self):
        self.name = "Pu'er tea"
class Tieguanyin(Tea):
    def __init__(self):
        self.name = "Tieguanyin"
class FourSeasonsSpringTea(Tea):
    def __init__(self):
        self.name = "Four seasons spring tea"
class JasmineGreenTea(Tea):
    def __init__(self):
        self.name = "Jasmine green tea"
class LongjingTea(Tea):
    def __init__(self):
        self.name = "Longjing tea"
class HoneyGrapefruitTea(Tea):
    def __init__(self):
        self.name = "Honey and grapefruit tea"
class LemonGrapefruitTea(Tea):
    def __init__(self):
        self.name = "Lemon and grapefruit tea"
class Biluochun(Tea):
    def __init__(self):
        self.name = "Biluochun"
class IceOolong(Tea):
    def __init__(self):
        self.name = "Ice oolong"


class MilkTea(Beverage):
    type = "MILKTEA"


class OriginalMilkTea(MilkTea):
    def __init__(self):
        self.name = "Original milk tea"
class MatchaMilkTea(MilkTea):
    def __init__(self):
        self.name = "Matcha milk tea"
class ChocolateMilkTea(MilkTea):
    def __init__(self):
        self.name = "Chocolate milk tea"
class BubbleTea(MilkTea):
    def __init__(self):
        self.name = "Bubble tea"
class OreoMilkTea(MilkTea):
    def __init__(self):
        self.name = "Oreo milk tea"
class RedBeanMilkTea(MilkTea):
    def __init__(self):
        self.name = "Red Bean milk tea"
class MatchaRedBean(MilkTea):
    def __init__(self):
        self.name = "Matcha red bean"
class CoconutFlavoredMilkTea(MilkTea):
    def __init__(self):
        self.name = "Coconut flavored tea"
class OriginalMilkGreen(MilkTea):
    def __init__(self):
        self.name = "Original milk green"
class JasmineMilkGreen(MilkTea):
    def __init__(self):
        self.name = "Jasmine milk green"


class Juice(Beverage):
    type = "JUICE"


class AppleJuice(Juice):
    def __init__(self):
        self.name = "Apple juice"
class LemonJuice(Juice):
    def __init__(self):
        self.name = "Lemon juice"
class WatermelonJuice(Juice):
    def __init__(self):
        self.name = "Watermelon juice"
class OrangeJuice(Juice):
    def __init__(self):
        self.name = "Orange juice"
class GrapeJuice(Juice):
    def __init__(self):
        self.name = "Grape juice"
class MangoJuice(Juice):
    def __init__(self):
        self.name = "Mango juice"
class PearJuice(Juice):
    def __init__(self):
        self.name = "Pear juice"
class StrawberryJuice(Juice):
    def __init__(self):
        self.name = "Strawberry juice"
class CherryJuice(Juice):
    def __init__(self):
        self.name = "Cherry juice"
class PeachJuice(Juice):
    def __init__(self):
        self.name = "Peach juice"


class FruitTea(Beverage):
    type = "FRUIT-TEA"


class Yangzhiganlu(FruitTea):
    def __init__(self):
        self.name = "Yangzhiganlu"
class MultiMangoYangzhiganlu(FruitTea):
    def __init__(self):
        self.name = "Multi mango Yangzhiganlu"
class StrawberryCherryTea(FruitTea):
    def __init__(self):
        self.name = "Strawberry cherry tea"
class LemonGreenTea(FruitTea):
    def __init__(self):
        self.name = "Lemon Green tea"
class LemonBlackTea(FruitTea):
    def __init__(self):
        self.name = "Lemon black tea"
class ABucketOfFruitTea(FruitTea):
    def __init__(self):
        self.name = "a bucket of fruit tea"
class StrawberryYogurt(FruitTea):
    def __init__(self):
        self.name = "Strawberry yogurt"
class OneCupPassionFruit(FruitTea):
    def __init__(self):
        self.name = "One cup passion fruit"
class PeachesSpringAllTheYear(FruitTea):
    def __init__(self):
        self.name = "Peaches spring all the year"
class RawCoconutWatermelon(FruitTea):
    def __init__(self):
        self.name = "Raw coconut watermelon"


class Coffee(Beverage):
    type = "COFFEE"

class StandardAmericanCoffee(Coffee):
    def __init__(self):
        self.name = "Standard American coffee"
class KappaCoffee(Coffee):
    def __init__(self):
        self.name = "Kappa coffee"
class LatteCoffee(Coffee):
    def __init__(self):
        self.name = "Latte coffee"
class RawCoconutLatte(Coffee):
    def __init__(self):
        self.name = "Raw coconut latte"
class ThickMilkLatte(Coffee):
    def __init__(self):
        self.name = "Thick milk latte"
class StrawberryIceLatte(Coffee):
    def __init__(self):
        self.name = "Strawberry ice latte"
class SnowTopCoffee(Coffee):
    def __init__(self):
        self.name = "Snow top coffee"
class IceCreamCoffee(Coffee):
    def __init__(self):
        self.name = "Ice cream coffee"
class MochaCoffee(Coffee):
    def __init__(self):
        self.name = "Mocha coffee"
class MatchaCoffee(Coffee):
    def __init__(self):
        self.name = "Matcha coffee"


class Smoothie(Beverage):
    type = "SMOOTHIE"

class StrawberryCustard(Smoothie):
    def __init__(self):
        self.name = "Strawberry custard"
class GrapeCustard(Smoothie):
    def __init__(self):
        self.name = "Grape custard"
class StrawberryMilkshake(Smoothie):
    def __init__(self):
        self.name = "Strawberry milkshake"
class PeachSmoothie(Smoothie):
    def __init__(self):
        self.name = "Peach smoothie"
class CreamySmoothie(Smoothie):
    def __init__(self):
        self.name = "Creamy smoothie"
class WatermelonSmoothie(Smoothie):
    def __init__(self):
        self.name = "Watermelon smoothie"
class MangoShavedIce(Smoothie):
    def __init__(self):
        self.name = "Mango shaved ice"
class StrawberryShavedIce(Smoothie):
    def __init__(self):
        self.name = "Strawberry shaved ice"
class HamiMelonShavedIce(Smoothie):
    def __init__(self):
        self.name = "Hami melon shaved ice"
class LemonSorbet(Smoothie):
    def __init__(self):
        self.name = "Lemon sorbet"

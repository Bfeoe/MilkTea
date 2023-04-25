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
        self.name = "红茶"


class PuerTea(Tea):
    def __init__(self):
        self.name = "普洱茶"


class TieGuanYin(Tea):
    def __init__(self):
        self.name = "铁观音"


class FourSeasonsSpringTea(Tea):
    def __init__(self):
        self.name = "四季春茶"


class JasmineGreenTea(Tea):
    def __init__(self):
        self.name = "茉莉绿茶"


class LongJingTea(Tea):
    def __init__(self):
        self.name = "龙井茶"


class HoneyGrapefruitTea(Tea):
    def __init__(self):
        self.name = "蜂蜜柚子茶"


class LemonGrapefruitTea(Tea):
    def __init__(self):
        self.name = "柠檬柚子茶"


class BiLuoChun(Tea):
    def __init__(self):
        self.name = "碧螺春"


class IceOolong(Tea):
    def __init__(self):
        self.name = "冰乌龙"


class MilkTea(Beverage):
    type = "MILKTEA"


class OriginalMilkTea(MilkTea):
    def __init__(self):
        self.name = "原味奶茶"


class MatchaMilkTea(MilkTea):
    def __init__(self):
        self.name = "抹茶奶茶"


class ChocolateMilkTea(MilkTea):
    def __init__(self):
        self.name = "巧克力奶茶"


class BubbleTea(MilkTea):
    def __init__(self):
        self.name = "珍珠奶茶"


class OreoMilkTea(MilkTea):
    def __init__(self):
        self.name = "奥利奥奶茶"


class RedBeanMilkTea(MilkTea):
    def __init__(self):
        self.name = "红豆奶茶"


class MatchaRedBean(MilkTea):
    def __init__(self):
        self.name = "抹茶红豆"


class CoconutFlavoredMilkTea(MilkTea):
    def __init__(self):
        self.name = "椰香奶茶"


class OriginalMilkGreen(MilkTea):
    def __init__(self):
        self.name = "原味奶绿"


class JasmineMilkGreen(MilkTea):
    def __init__(self):
        self.name = "茉莉奶绿"


class Juice(Beverage):
    type = "JUICE"


class AppleJuice(Juice):
    def __init__(self):
        self.name = "苹果汁"


class LemonJuice(Juice):
    def __init__(self):
        self.name = "柠檬汁"


class WatermelonJuice(Juice):
    def __init__(self):
        self.name = "西瓜汁"


class OrangeJuice(Juice):
    def __init__(self):
        self.name = "橘子汁"


class GrapeJuice(Juice):
    def __init__(self):
        self.name = "葡萄汁"


class MangoJuice(Juice):
    def __init__(self):
        self.name = "芒果汁"


class PearJuice(Juice):
    def __init__(self):
        self.name = "梨子汁"


class StrawberryJuice(Juice):
    def __init__(self):
        self.name = "草莓汁"


class CherryJuice(Juice):
    def __init__(self):
        self.name = "樱桃汁"


class PeachJuice(Juice):
    def __init__(self):
        self.name = "桃子汁"


class FruitTea(Beverage):
    type = "FRUIT-TEA"


class YangZhiGanLu(FruitTea):
    def __init__(self):
        self.name = "杨枝甘露"


class MultiMangoYangZhiGanLu(FruitTea):
    def __init__(self):
        self.name = "多芒杨枝甘露"


class StrawberryCherryTea(FruitTea):
    def __init__(self):
        self.name = "草莓樱桃茶"


class LemonGreenTea(FruitTea):
    def __init__(self):
        self.name = "柠檬绿茶"


class LemonBlackTea(FruitTea):
    def __init__(self):
        self.name = "柠檬红茶"


class ABucketOfFruitTea(FruitTea):
    def __init__(self):
        self.name = "一桶水果茶"


class StrawberryYogurt(FruitTea):
    def __init__(self):
        self.name = "草莓酸奶"


class OneCupPassionFruit(FruitTea):
    def __init__(self):
        self.name = "一杯百香果"


class PeachesSpringAllTheYear(FruitTea):
    def __init__(self):
        self.name = "蜜桃四季春"


class RawCoconutWatermelon(FruitTea):
    def __init__(self):
        self.name = "生椰西瓜"


class Coffee(Beverage):
    type = "COFFEE"


class StandardAmericanCoffee(Coffee):
    def __init__(self):
        self.name = "标准美式咖啡"


class KappaCoffee(Coffee):
    def __init__(self):
        self.name = "卡布咖啡"


class LatteCoffee(Coffee):
    def __init__(self):
        self.name = "拿铁咖啡"


class RawCoconutLatte(Coffee):
    def __init__(self):
        self.name = "生耶拿铁"


class ThickMilkLatte(Coffee):
    def __init__(self):
        self.name = "厚乳拿铁"


class StrawberryIceLatte(Coffee):
    def __init__(self):
        self.name = "草莓冰拿铁"


class SnowTopCoffee(Coffee):
    def __init__(self):
        self.name = "雪顶咖啡"


class IceCreamCoffee(Coffee):
    def __init__(self):
        self.name = "冰淇淋咖啡"


class MochaCoffee(Coffee):
    def __init__(self):
        self.name = "摩卡咖啡"


class MatchaCoffee(Coffee):
    def __init__(self):
        self.name = "抹茶咖啡"


class Smoothie(Beverage):
    type = "SMOOTHIE"


class StrawberryCustard(Smoothie):
    def __init__(self):
        self.name = "草莓奶冻"


class GrapeCustard(Smoothie):
    def __init__(self):
        self.name = "葡萄奶冻"


class StrawberryMilkshake(Smoothie):
    def __init__(self):
        self.name = "草莓奶昔"


class PeachSmoothie(Smoothie):
    def __init__(self):
        self.name = "蜜桃奶昔"


class CreamySmoothie(Smoothie):
    def __init__(self):
        self.name = "奶香冰沙"


class WatermelonSmoothie(Smoothie):
    def __init__(self):
        self.name = "西瓜冰沙"


class MangoShavedIce(Smoothie):
    def __init__(self):
        self.name = "芒果刨冰"


class StrawberryShavedIce(Smoothie):
    def __init__(self):
        self.name = "草莓刨冰"


class HamiMelonShavedIce(Smoothie):
    def __init__(self):
        self.name = "哈密瓜刨冰"


class LemonSorbet(Smoothie):
    def __init__(self):
        self.name = "柠檬冰沙"

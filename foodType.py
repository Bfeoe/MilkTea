class Beverage:
    name = ''
    price: float = 0.0
    type = ""
    heat = ''
    cup = ''
    material = []

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

    def setHeat(self, heat):
        if self.heat != '' and self.heat != heat:
            print(f"这个产品只能做成 {self.heat}饮 !")
        else:
            self.heat = heat

    def getHeat(self):
        return self.heat

    def setCup(self, cup):
        if self.cup != '' and self.cup != cup:
            print(f"这个产品只有 {self.cup} ！")
        else:
            self.cup = cup

    def getCup(self):
        return self.cup

    def getSugar(self):
        return self.sugar

    def setSugar(self, sugar):
        self.sugar = sugar


class Tea(Beverage):
    type = "TEA"
    cup = '小杯'


class BlackTea(Tea):
    material = ["black tea"]
    def __init__(self):
        self.name = "红茶"


class PuerTea(Tea):
    heat = '热'
    material = ["Puer tea"]
    def __init__(self):
        self.name = "普洱茶"


class TieGuanYin(Tea):
    heat = '热'
    material = ["Tieguanyin"]
    def __init__(self):
        self.name = "铁观音"


class FourSeasonsSpringTea(Tea):
    material = ["oolong"]
    def __init__(self):
        self.name = "四季春茶"


class JasmineGreenTea(Tea):
    material = ["green tea",
                "jasmine"]
    def __init__(self):
        self.name = "茉莉绿茶"


class LongJingTea(Tea):
    heat = '热'
    material = ["Longjing tea"]
    def __init__(self):
        self.name = "龙井茶"


class HoneyGrapefruitTea(Tea):
    material = ["honey", "grapefruit", "tea"]
    def __init__(self):
        self.name = "蜂蜜柚子茶"


class LemonGrapefruitTea(Tea):
    material = ["lemon", "grapefruit", "tea"]
    def __init__(self):
        self.name = "柠檬柚子茶"


class BiLuoChun(Tea):
    heat = '热'
    material = ["Biluochun"]
    def __init__(self):
        self.name = "碧螺春"


class IceOolong(Tea):
    heat = '冷'
    material = ["ice oolong"]
    def __init__(self):
        self.name = "冰乌龙"


class MilkTea(Beverage):
    type = "MILKTEA"


class OriginalMilkTea(MilkTea):
    material = ["milk", "tea"]
    def __init__(self):
        self.name = "原味奶茶"


class MatchaMilkTea(MilkTea):
    material = ["milk", "Matcha"]
    def __init__(self):
        self.name = "抹茶奶茶"


class ChocolateMilkTea(MilkTea):
    material = ["milk", "tea", "chocolate"]
    def __init__(self):
        self.name = "巧克力奶茶"


class BubbleTea(MilkTea):
    material = ["milk", "tea", "Bobble"]
    def __init__(self):
        self.name = "珍珠奶茶"


class OreoMilkTea(MilkTea):
    material = ["milk", "tea", "Oreo"]
    def __init__(self):
        self.name = "奥利奥奶茶"


class RedBeanMilkTea(MilkTea):
    material = ["milk", "tea", "red bean"]
    def __init__(self):
        self.name = "红豆奶茶"


class MatchaRedBean(MilkTea):
    material = ["milk", "Matcha", "red bean"]
    def __init__(self):
        self.name = "抹茶红豆"


class CoconutFlavoredMilkTea(MilkTea):
    material = ["milk", "tea", "coconut"]
    def __init__(self):
        self.name = "椰香奶茶"


class OriginalMilkGreen(MilkTea):
    material = ["milk", "green tea"]
    def __init__(self):
        self.name = "原味奶绿"


class JasmineMilkGreen(MilkTea):
    material = ["milk", "green tea", "jasmine"]
    def __init__(self):
        self.name = "茉莉奶绿"


class Juice(Beverage):
    type = "JUICE"


class AppleJuice(Juice):
    material = ["apple"]
    def __init__(self):
        self.name = "苹果汁"


class LemonJuice(Juice):
    material = ["lemon"]
    def __init__(self):
        self.name = "柠檬汁"


class WatermelonJuice(Juice):
    material = ["watermelon"]
    def __init__(self):
        self.name = "西瓜汁"


class OrangeJuice(Juice):
    material = ["orange"]
    def __init__(self):
        self.name = "橘子汁"


class GrapeJuice(Juice):
    material = ["grape"]
    def __init__(self):
        self.name = "葡萄汁"


class MangoJuice(Juice):
    material = ["mango"]
    def __init__(self):
        self.name = "芒果汁"


class PearJuice(Juice):
    material = ["pear"]
    def __init__(self):
        self.name = "梨子汁"


class StrawberryJuice(Juice):
    material = ["strawberry"]
    def __init__(self):
        self.name = "草莓汁"


class CherryJuice(Juice):
    material = ["cherry"]
    def __init__(self):
        self.name = "樱桃汁"


class PeachJuice(Juice):
    material = ["peach"]
    def __init__(self):
        self.name = "桃子汁"


class FruitTea(Beverage):
    type = "FRUIT-TEA"
    heat = '冷'


class YangZhiGanLu(FruitTea):
    material = ["tea", "mango", "tea"]
    def __init__(self):
        self.name = "杨枝甘露"


class MultiMangoYangZhiGanLu(FruitTea):
    cup = '大杯'
    material = ["tea", "mango", "tea"]
    def __init__(self):
        self.name = "多芒杨枝甘露"


class StrawberryCherryTea(FruitTea):
    material = ["strawberry", "cherry", "tea"]
    def __init__(self):
        self.name = "草莓樱桃茶"


class LemonGreenTea(FruitTea):
    material = ["cherry", "yogurt"]
    def __init__(self):
        self.name = "柠檬绿茶"


class LemonBlackTea(FruitTea):
    material = ["lemon", "black tea"]
    def __init__(self):
        self.name = "柠檬红茶"


class ABucketOfFruitTea(FruitTea):
    cup = '大杯'
    material = ["tea", "strawberry", "cherry", "peach", "watermelon"]
    def __init__(self):
        self.name = "一桶水果茶"


class StrawberryYogurt(FruitTea):
    material = ["strawberry", "yogurt"]
    def __init__(self):
        self.name = "草莓酸奶"


class OneCupPassionFruit(FruitTea):
    material = ["tea", "passion fruit"]
    def __init__(self):
        self.name = "一杯百香果"


class PeachesSpringAllTheYear(FruitTea):
    material = ["tea", "peach"]
    def __init__(self):
        self.name = "蜜桃四季春"


class RawCoconutWatermelon(FruitTea):
    material = ["tea", "coconut", "watermelon"]
    def __init__(self):
        self.name = "生椰西瓜"


class Coffee(Beverage):
    type = "COFFEE"


class StandardAmericanCoffee(Coffee):
    material = ["coffee"]
    def __init__(self):
        self.name = "标准美式咖啡"


class KappaCoffee(Coffee):
    material = ["coffee", "milk"]
    def __init__(self):
        self.name = "卡布咖啡"


class LatteCoffee(Coffee):
    material = ["coffee", "milk"]
    def __init__(self):
        self.name = "拿铁咖啡"


class RawCoconutLatte(Coffee):
    material = ["coffee", "milk", "coconut"]
    def __init__(self):
        self.name = "生耶拿铁"


class ThickMilkLatte(Coffee):
    material = ["coffee", "milk", "cream"]
    def __init__(self):
        self.name = "厚乳拿铁"


class StrawberryIceLatte(Coffee):
    heat = '冷'
    material = ["coffee", "milk", "strawberry"]
    def __init__(self):
        self.name = "草莓冰拿铁"


class SnowTopCoffee(Coffee):
    heat = '冷'
    material = ["coffee", "milk", "cream"]
    def __init__(self):
        self.name = "雪顶咖啡"


class IceCreamCoffee(Coffee):
    heat = '冷'
    material = ["coffee", "milk", "icecream"]
    def __init__(self):
        self.name = "冰淇淋咖啡"


class MochaCoffee(Coffee):
    material = ["coffee", "milk", "chocolate"]
    def __init__(self):
        self.name = "摩卡咖啡"


class MatchaCoffee(Coffee):
    material = ["coffee", "Matcha"]
    def __init__(self):
        self.name = "抹茶咖啡"


class Smoothie(Beverage):
    type = "SMOOTHIE"
    heat = '冷'
    cup = '小杯'


class StrawberryCustard(Smoothie):
    material = ["strawberry", "milk"]
    def __init__(self):
        self.name = "草莓奶冻"


class GrapeCustard(Smoothie):
    material = ["grape", "milk"]
    def __init__(self):
        self.name = "葡萄奶冻"


class StrawberryMilkshake(Smoothie):
    material = ["strawberry", "milk", "icecream"]
    def __init__(self):
        self.name = "草莓奶昔"


class PeachSmoothie(Smoothie):
    material = ["peach", "milk", "icecream"]
    def __init__(self):
        self.name = "蜜桃奶昔"


class CreamySmoothie(Smoothie):
    material = ["cream"]
    def __init__(self):
        self.name = "奶香冰沙"


class WatermelonSmoothie(Smoothie):
    material = ["watermelon"]
    def __init__(self):
        self.name = "西瓜冰沙"


class MangoShavedIce(Smoothie):
    material = ["mango"]
    def __init__(self):
        self.name = "芒果刨冰"


class StrawberryShavedIce(Smoothie):
    material = ["strawberry"]
    def __init__(self):
        self.name = "草莓刨冰"


class HamiMelonShavedIce(Smoothie):
    material = ["hami melon"]
    def __init__(self):
        self.name = "哈密瓜刨冰"


class LemonSorbet(Smoothie):
    material = ["lemon"]
    def __init__(self):
        self.name = "柠檬冰沙"

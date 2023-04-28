from foodType import *


class foodFactory():
    translation = {"原味奶茶": "OriginalMilkTea", "抹茶奶茶": "MatchaMilkTea", "巧克力奶茶": "ChocolateMilkTea",
                   "珍珠奶茶": "BubbleTea", "奥利奥奶茶": "OreoMilkTea",
                   "红豆奶茶": "RedBeanMilkTea", "抹茶红豆": "MatchaRedBean", "椰香奶茶": "CoconutFlavoredMilkTea",
                   "原味奶绿": "OriginalMilkGreen", "茉莉奶绿": "JasmineMilkGreen",
                   "标准美式": "StandardAmericanCoffee", "卡布咖啡": "KappaCoffee", "拿铁咖啡": "LatteCoffee",
                   "生椰拿铁": "RawCoconutLatte", "厚乳拿铁": "ThickMilkLatte",
                   "草莓冰拿铁": "StrawberryIceLatte", "雪顶咖啡": "SnowTopCoffee", "冰淇淋咖啡": "IceCreamCoffee",
                   "摩卡咖啡": "MochaCoffee", "抹茶咖啡": "MatchaCoffee",
                   "杨枝甘露": "YangZhiGanLu", "葡萄多多": "GrapeMore", "草莓樱桃茶": "StrawberryCherryTea",
                   "草莓酸奶": "StrawberryYogurt", "一杯百香果": "OneCupPassionFruit",
                   "蜜桃四季春": "PeachesSpringAllTheYear", "生椰西瓜": "RawCoconutWatermelon", "柠檬绿茶": "LemonGreenTea",
                   "柠檬红茶": "LemonBlackTea", "一桶水果茶": "ABucketOfFruitTea",
                   "草莓奶冻": "StrawberryCustard", "葡萄奶冻": "GrapeCustard", "草莓奶昔": "StrawberryMilkshake",
                   "水蜜桃奶昔": "PeachSmoothie", "芒果刨冰": "MangoShavedIce",
                   "草莓刨冰": "StrawberryShavedIce", "哈密瓜刨冰": "HamiMelonShavedIce", "柠檬冰沙": "LemonSorbet",
                   "奶香冰沙": "CreamySmoothie", "西瓜冰沙": "WatermelonSmoothie",
                   "苹果汁": "AppleJuice", "柠檬汁": "LemonJuice", "西瓜汁": "WatermelonJuice",
                   "橙汁": "OrangeJuice", "葡萄汁": "GrapeJuice",
                   "芒果汁": "MangoJuice", "梨汁": "PearJuice", "草莓汁": "StrawberryJuice",
                   "樱桃汁": "CherryJuice", "桃子汁": "PeachJuice"
                   }
    def make(self, pname):
        eName = self.translation.get(pname)
        return eval(eName + '()')
#
#
# class milkTeaFactory(foodFactory):
#     translation = {"原味奶茶": "OriginalMilkTea",
#                    "抹茶奶茶": "MatchaMilkTea",
#                    "巧克力奶茶": "ChocolateMilkTea",
#                    "珍珠奶茶": "BubbleTea",
#                    "奥利奥奶茶": "OreoMilkTea",
#                    "红豆奶茶": "RedBeanMilkTea",
#                    "抹茶红豆": "MatchaRedBean",
#                    "椰香奶茶": "CoconutFlavoredMilkTea",
#                    "原味奶绿": "OriginalMilkGreen",
#                    "茉莉奶绿": "JasmineMilkGreen",
#                    "四季春茶": "FourSeasonsSpringTea",
#                    "茉莉绿茶": "JasmineGreenTea",
#                    "龙井茶": "LongJingTea",
#                    "碧螺春": "BiLuoChun",
#                    "蜂蜜柚子茶": "HoneyGrapefruitTea",
#                    "柠檬柚子茶": "LemonGrapefruitTea",
#                    "红茶": "BlackTea",
#                    "普洱茶": "PuerTea",
#                    "铁观音": "TieGuanYin",
#                    "冰乌龙": "IceOolong",
#                    }
#
#     def __init__(self):
#         self.type = "MILKTEA"
#
#
# class coffeeFactory(foodFactory):
#     translation = {"标准美式": "StandardAmericanCoffee",
#                    "卡布咖啡": "KappaCoffee",
#                    "拿铁咖啡": "LatteCoffee",
#                    "生椰拿铁": "RawCoconutLatte",
#                    "厚乳拿铁": "ThickMilkLatte",
#                    "草莓冰拿铁": "StrawberryIceLatte",
#                    "雪顶咖啡": "SnowTopCoffee",
#                    "冰淇淋咖啡": "IceCreamCoffee",
#                    "摩卡咖啡": "MochaCoffee",
#                    "抹茶咖啡": "MatchaCoffee"
#                    }
#
#     def __init__(self):
#         self.type = "COFFEE"
#
#
# class teaFactory(foodFactory):
#     translation = {"四季春茶": "FourSeasonsSpringTea",
#                    "茉莉绿茶": "JasmineGreenTea",
#                    "龙井茶": "LongJingTea",
#                    "碧螺春": "BiLuoChun",
#                    "蜂蜜柚子茶": "HoneyGrapefruitTea",
#                    "柠檬柚子茶": "LemonGrapefruitTea",
#                    "红茶": "BlackTea",
#                    "普洱茶": "PuerTea",
#                    "铁观音": "TieGuanYin",
#                    "冰乌龙": "IceOolong"
#                    }
#
#     def __init__(self):
#         self.type = "TEA"
#
#
# class fruitTeaFactory(foodFactory):
#     translation = {"杨枝甘露": "YangZhiGanLu",
#                    "葡萄多多": "GrapeMore",
#                    "草莓樱桃茶": "StrawberryCherryTea",
#                    "草莓酸奶": "StrawberryYogurt",
#                    "一杯百香果": "OneCupPassionFruit",
#                    "蜜桃四季春": "PeachesSpringAllTheYear",
#                    "生椰西瓜": "RawCoconutWatermelon",
#                    "柠檬绿茶": "LemonGreenTea",
#                    "柠檬红茶": "LemonBlackTea",
#                    "一桶水果茶": "ABucketOfFruitTea"
#                    }
#
#     def __init__(self):
#         self.type = "FRUIT-TEA"
#
#
# class smoothieFactory(foodFactory):
#     translation = {"草莓奶冻": "StrawberryCustard",
#                    "葡萄奶冻": "GrapeCustard",
#                    "草莓奶昔": "StrawberryMilkshake",
#                    "水蜜桃奶昔": "PeachSmoothie",
#                    "芒果刨冰": "MangoShavedIce",
#                    "草莓刨冰": "StrawberryShavedIce",
#                    "哈密瓜刨冰": "HamiMelonShavedIce",
#                    "柠檬冰沙": "LemonSorbet",
#                    "奶香冰沙": "CreamySmoothie",
#                    "西瓜冰沙": "WatermelonSmoothie"
#                    }
#
#     def __init__(self):
#         self.type = "SMOOTHIE"
#
#
# class juiceFactory(foodFactory):
#     translation = {"苹果汁": "AppleJuice",
#                    "柠檬汁": "LemonJuice",
#                    "西瓜汁": "WatermelonJuice",
#                    "橙汁": "OrangeJuice",
#                    "葡萄汁": "GrapeJuice",
#                    "芒果汁": "MangoJuice",
#                    "梨汁": "PearJuice",
#                    "草莓汁": "StrawberryJuice",
#                    "樱桃汁": "CherryJuice",
#                    "桃子汁": "PeachJuice"
#                    }
#
#     def __init__(self):
#         self.type = "JUICE"
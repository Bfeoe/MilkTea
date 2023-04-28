from foodFactory import *


class menuAll:
    menu_map = dict()

    def loadMenu(self):
        self.menu_map["beverage"] = ["原味奶茶", "抹茶奶茶", "巧克力奶茶", "珍珠奶茶", "奥利奥奶茶",
                                     "红豆奶茶", "抹茶红豆", "椰香奶茶", "原味奶绿", "茉莉奶绿",
                                     "草莓奶冻", "葡萄奶冻", "草莓奶昔", "水蜜桃奶昔", "芒果刨冰",
                                     "草莓刨冰", "哈密瓜刨冰", "柠檬冰沙", "奶香冰沙", "西瓜冰沙",
                                     "四季春茶", "茉莉绿茶", "龙井茶", "碧螺春", "蜂蜜柚子茶",
                                     "柠檬柚子茶", "红茶", "普洱茶", "铁观音", "冰乌龙",
                                     "标准美式", "卡布咖啡", "拿铁咖啡", "生椰拿铁", "厚乳拿铁",
                                     "草莓冰拿铁", "雪顶咖啡", "冰淇淋咖啡", "摩卡咖啡", "抹茶咖啡",
                                     "杨枝甘露", "葡萄多多", "草莓樱桃茶", "草莓酸奶", "一杯百香果",
                                     "蜜桃四季春", "生椰西瓜", "柠檬绿茶", "柠檬红茶", "一桶水果茶",
                                     "苹果汁", "柠檬汁", "西瓜汁", "橙汁", "葡萄汁",
                                     "芒果汁", "梨汁", "草莓汁", "樱桃汁", "桃子汁"]
        self.menu_map["sugar"] = ["正常糖", "七分糖", "半糖,""三分糖", "无糖"]
        self.menu_map["heat"] = ["正常冰", "常温", "少冰", "去冰", "热饮"]
        self.menu_map["xiao liao"] = ["西米", "椰果", "珍珠", "芋泥", "芋圆", "奶冻", "糯米", "奥利奥", "麻薯", "奶盖",
                                      "冰激凌"]
        self.menu_map["size"] = ["大杯", "小杯"]

    def isBeverage(self, dish):
        if dish in self.menu_map["beverage"]:
            return True
        return False

    def isSugar(self, dish):
        if dish in self.menu_map["sugar"]:
            return True
        return False

    def isHeat(self, dish):
        if dish in self.menu_map["heat"]:
            return True
        return False

    def isXiaoLiao(self, dish):
        if dish in self.menu_map["xiao liao"]:
            return True
        return False

    def isSize(self, dish):
        if dish in self.menu_map["size"]:
            return True
        return False

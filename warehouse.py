class Warehouse:
    ware_name = ""
    goods = {}
    threshold = 0.0

    def setThreshold(self, threshold):
        self.threshold = threshold

    def notify(self):
        for name, num in self.goods.values():
            if num <= self.threshold:
                print(f"{self.ware_name}中的{name}不够了！")
                return False
            else:
                return True


class MilkWarehouse(Warehouse):
    ware_name = "MilkWarehouse"
    goods = {"milk": 1500,
             "yogurt": 1500,
             "coffee:": 3000,
             "chocolate": 1500,
             }


class TeaWarehouse(Warehouse):
    ware_name = "TeaWarehouse"
    goods = {"tea": 3000,
             "green tea": 1500,
             "black tea": 1500,
             "Matcha": 1500,
             "oolong": 1500,
             "jasmine tea": 1500,
             "Longjing tea": 1500,
             "Biluochun": 1500,
             "Pu'er tea": 1500,
             "Tieguanyin": 1500
             }


class FruitWarehouse(Warehouse):
    ware_name = "FruitWarehouse"
    goods = {"apple": 20,
             "lemon": 20,
             "watermelon": 20,
             "orange": 20,
             "grape": 20,
             "mango": 20,
             "pear": 20,
             "strawberry": 20,
             "cherry": 20,
             "peach": 20,
             "grapefruit": 20,
             "passion fruit": 20,
             "hami melon": 20
             }


class IngredientWarehouse(Warehouse):
    ware_name = "IngredientWarehouse"
    goods = {"bubble": 15,
             "Oreo": 15,
             "red bean": 15,
             "honey": 15,
             "cream": 15,
             "coconut": 15,
             "ice cream": 15,
             "sago": 15,
             "mashed taro": 15,
             "taro ball": 15,
             "sticky rice": 15,
             "mochi": 15,
             "custard": 15
             }

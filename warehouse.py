class Warehouse:
    ware_name = ""
    goods = {}
    unit_price = {}
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
    threshold = 350
    ware_name = "MilkWarehouse"
    goods = {"milk": 1500,
             "yogurt": 1500,
             "coffee:": 3000,
             }
    unit_price = {"milk": 2,
                  "yogurt": 3,
                  "coffee:": 4,
                  }


class TeaWarehouse(Warehouse):
    threshold = 350
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
    unit_price = {"tea": 2,
                  "green tea": 3,
                  "black tea": 3,
                  "Matcha": 3,
                  "oolong": 6,
                  "Longjing tea": 7,
                  "Biluochun": 4,
                  "Pu'er tea": 4,
                  "Tieguanyin": 6
                  }


class FruitWarehouse(Warehouse):
    threshold = 1
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
    unit_price = {"apple": 1,
                  "lemon": 1,
                  "watermelon": 1,
                  "orange": 1,
                  "grape": 1,
                  "mango": 1,
                  "pear": 1,
                  "strawberry": 1.5,
                  "cherry": 1.5,
                  "peach": 1,
                  "grapefruit": 1,
                  "passion fruit": 2,
                  "hami melon": 1
                  }


class IngredientWarehouse(Warehouse):
    threshold = 1
    ware_name = "IngredientWarehouse"
    goods = {"bubble": 15,
             "Oreo": 15,
             "red bean": 15,
             "honey": 15,
             "cream": 15,
             "coconut": 15,
             "chocolate": 15,
             "ice cream": 15,
             "sago": 15,
             "mashed taro": 15,
             "taro ball": 15,
             "sticky rice": 15,
             "mochi": 15,
             "custard": 15
             }
    unit_price = {"bubble": 1,
                  "Oreo": 2,
                  "red bean": 1,
                  "honey": 2,
                  "cream": 2,
                  "coconut": 1,
                  "chocolate": 2,
                  "ice cream": 6,
                  "sago": 1,
                  "mashed taro": 2,
                  "taro ball": 2,
                  "sticky rice": 2,
                  "mochi": 3,
                  "custard": 2,
                  "jasmine": 1
                  }

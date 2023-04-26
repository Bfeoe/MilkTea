class foodFactory():
    type = ""

    def createFood(self, foodClass):
        foodIns = foodClass()
        return foodIns


class milkTeaFactory(foodFactory):
    def __init__(self):
        self.type = "MILKTEA"


class coffeeFactory(foodFactory):
    def __init__(self):
        self.type = "COFFEE"


class teaFactory(foodFactory):
    def __init__(self):
        self.type = "TEA"


class fruitTeaFactory(foodFactory):
    def __init__(self):
        self.type = "FRUITTEA"


class smoothieFactory(foodFactory):
    def __init__(self):
        self.type = "SMOOTHIE"


class juiceFactory(foodFactory):
    def __init__(self):
        self.type = "JUICE"

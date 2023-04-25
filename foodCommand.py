class cookSys():
    def cook(self, dish):
        pass


class milkTeaSys(cookSys):
    def cook(self, dish):
        print("MILKTEA:Cook %s" % dish)


class juiceSys(cookSys):
    def cook(self, dish):
        print("COOLDISH:Cook %s" % dish)


class fruitTeaSys(cookSys):
    def cook(self, dish):
        print("HOTDISH:Cook %s" % dish)


class teaSys(cookSys):
    def cook(self, dish):
        print("HOTDISH:Cook %s" % dish)


class coffeeSys(cookSys):
    def cook(self, dish):
        print("HOTDISH:Cook %s" % dish)


class smoothie(cookSys):
    def cook(self, dish):
        print("HOTDISH:Cook %s" % dish)

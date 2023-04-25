from foodFactory import juiceFactory, milkTeaFactory
from foodType import AppleJuice, OriginalMilkTea

if __name__ == "__main__":
    juice_factory = juiceFactory()
    milkTea_factory = milkTeaFactory()
    apple_juice = juice_factory.createFood(AppleJuice)
    print(apple_juice.getName(), apple_juice.getPrice())
    original_milk_tea = milkTea_factory.createFood(OriginalMilkTea)
    print(original_milk_tea.getName(), original_milk_tea.getPrice())

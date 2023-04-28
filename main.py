import tkinter
from foodType import *
from munuAll import menuAll
from orderBuilder import OrderBuilder

root = tkinter.Tk()
root.title("奶茶店菜单")
img_gif = tkinter.PhotoImage(file='C:\\Users\\John Nash\\Desktop\\MilkTea\\menu.gif')
label_img = tkinter.Label(root, image=img_gif)
label_img.pack()
root.mainloop()

order_builder = OrderBuilder()

dish_list = list(input("顾客您好，请您点单！\n").split())

if __name__ == "__main__":
    menu = menuAll()
    menu.loadMenu()
    for dish in dish_list:
        if menu.isBeverage(dish):
            order_builder.setBeverage(dish)
        elif menu.isSize(dish):
            order_builder.setCup(dish)
        elif menu.isHeat(dish):
            order_builder.setHeat(dish)
        elif menu.isSugar(dish):
            order_builder.setSugar(dish)
        else:
            continue

    order_1 = order_builder.build()
    order_1.show()

# if __name__ == "__main__":
#     milkTea_factory = milkTeaFactory()
#     apple_juice = juice_factory.createFood(AppleJuice)
#     print(apple_juice.getName(), apple_juice.getPrice())
#     original_milk_tea = milkTea_factory.createFood(OriginalMilkTea)
#     print(original_milk_tea.getName(), original_milk_tea.getPrice())

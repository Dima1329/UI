from tkinter import *
from UIButton import *
from UIElementBoundaries import *
from UIInfo import *
from UIMainStack import UIMainStack
from UIMenu import UIMenu

window = Tk()
canvas = Canvas(window, width=500, height=500, )
canvas.pack()
menu_stack = UIMainStack()
canvas.create_rectangle(0, 0, 500, 500, fill="grey")

bounderies1 = UIElementBoundaries(10, 10, 490, 40)
element1 = UIButton("black", "white", "Button", canvas, bounderies1, lambda: print("Done Button"))

bounderies2 = UIElementBoundaries(10, 40, 490, 70)
element2 = UIInfo("black", "white", "Info", canvas, bounderies2)

elementm11 = UIInfo("black", "white", "I1", canvas, bounderies1)
elementm12 = UIInfo("black", "white", "I2", canvas, bounderies2)
windowelements1 = [elementm11, elementm12]  # 3

bounderies3 = UIElementBoundaries(10, 70, 490, 100)
elementm1 = UIInfo("black", "white", "I1", canvas, bounderies1)
elementm2 = UIInfo("black", "white", "I2", canvas, bounderies2)
elementm3 = UIMenu("black", "white", "M1", canvas, bounderies3, windowelements1, menu_stack)
windowelements = [elementm1, elementm2, elementm3]  # 2

element3 = UIMenu("black", "white", "Menushka", canvas, bounderies3, windowelements, menu_stack)

# 1

menu_stack.push([element1, element2, element3])


def move_select_or_do(e):
    menu_stack.get_menu()[menu_stack.get_state()].set_deselect()
    if e.keysym == 'Up':
        if menu_stack.get_state() == 0:
            menu_stack.set_state(len(menu_stack.get_menu()) - 1)
        else:
            menu_stack.set_state(menu_stack.get_state() - 1)
    elif e.keysym == 'Down':
        if menu_stack.get_state() + 1 == len(menu_stack.get_menu()):
            menu_stack.set_state(0)
        else:
            menu_stack.set_state(menu_stack.get_state() + 1)
    elif e.keysym == 'space':
        canvas.create_rectangle(0, 0, 500, 500, fill="grey")
        menu_stack.get_menu()[menu_stack.get_state()].do()

    elif e.keysym == "Left":
        menu_stack.pop()

    menu_stack.get_menu()[menu_stack.get_state()].set_select()


canvas.bind_all('<Key>', move_select_or_do)
element1.set_select()
while True:
    window.update()
    for i in menu_stack.get_menu():
        i.render()

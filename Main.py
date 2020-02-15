from tkinter import *
from UIButton import *
from UIElementBoundaries import *
from UIInfo import *
from UIMainStack import UIMainStack
from UIMenu import UIMenu
from UIScroll import UIScroller

window = Tk()
canvas = Canvas(window, width=500, height=110)
canvas.pack()
scroller = UIScroller()
menu_stack = UIMainStack(scroller)
scroller.set_stack(menu_stack)
canvas.create_rectangle(0, 0, 500, 110, fill="grey")
bounderies5 = UIElementBoundaries(10, 100000000, 490, 1000000000)

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
element4 = UIInfo("black", "white", "I11", canvas, bounderies5)
element5 = UIInfo("black", "white", "I12", canvas, bounderies5)
element6 = UIInfo("black", "white", "I13", canvas, bounderies5)
element7 = UIInfo("black", "white", "I14", canvas, bounderies5)

menu_stack.push([element1, element2, element4,element3,element5,element6,element7])


def move_select_or_do(e):
    menu_stack.get_menu()[menu_stack.get_state()].hide_everything()
    menu_stack.get_menu()[menu_stack.get_state()].set_deselect()
    if e.keysym == 'Up':
        if menu_stack.get_state() != 0:
            menu_stack.set_state(menu_stack.get_state() - 1)

    elif e.keysym == 'Down':
        if menu_stack.get_state() + 1 != len(menu_stack.get_menu()):
            menu_stack.set_state(menu_stack.get_state() + 1)

    elif e.keysym == 'space' or e.keysym == 'Right':

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



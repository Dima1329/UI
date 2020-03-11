from tkinter import *
from UIButton import *
from UIInfo import *
from UIMainStack import UIMainStack
from UIMenu import UIMenu
from UIScroll import *
from UIUpdaterOfBoundaries import *
window = Tk()
canvas = Canvas(window, width=500, height=110)
canvas.pack()
scroller = UIScroller()
menu_stack = UIMainStack()
updater = UIUpdaterOfBoundaries()
scroller.set_stack(menu_stack)
updater.set_stack(menu_stack)
canvas.create_rectangle(0, 0, 500, 110, fill="grey")
bounderies5 = UIElementBoundaries(10, 100000000, 490, 1000000000)


element1 = UIButton("black", "white", "Button", canvas, lambda: print("Done Button"))

element2 = UIInfo("black", "white", "Info", canvas)

elementm11 = UIElement("black", "white", "I1", canvas)
elementm12 = UIInfo("black", "white", "I2", canvas)
windowelements1 = [elementm11, elementm12]  # 3

elementm1 = UIInfo("black", "white", "I1", canvas)
elementm2 = UIInfo("black", "white", "I2", canvas)
elementm3 = UIMenu("black", "white", "M1", canvas, windowelements1, menu_stack, updater)
windowelements = [elementm1, elementm2, elementm3]  # 2

element3 = UIMenu("black", "white", "Menushka", canvas,  windowelements, menu_stack, updater)
element4 = UIInfo("black", "white", "I11", canvas)
element5 = UIInfo("black", "white", "I12", canvas)
element6 = UIInfo("black", "white", "I13", canvas)
element7 = UIInfo("black", "white", "I14", canvas)
menu_stack.push([element1, element2, element3,element4,element5,element6,element7])
scroller.update()


def move_select_or_do(e):
    menu_stack.get_menu()[menu_stack.get_state()].set_deselect()
    if e.keysym == 'Up':
        scroller.window_up()

    elif e.keysym == 'Down':
        scroller.window_down()

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

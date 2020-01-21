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
windowelements1 = [elementm11, elementm12]#3

bounderies3 = UIElementBoundaries(10, 70, 490, 100)
elementm1 = UIInfo("black", "white", "I1", canvas, bounderies1)
elementm2 = UIInfo("black", "white", "I2", canvas, bounderies2)
elementm3 = UIMenu("black", "white", "M1", canvas, bounderies3,windowelements1, menu_stack)
windowelements = [elementm1, elementm2, elementm3]#2

element3 = UIMenu("black", "white", "Menushka", canvas, bounderies3, windowelements, menu_stack)

elements = [element1, element2, element3]#1

menu_stack.push(elements)
def move_select_or_do(e):
    global selected_element
    global elements
    elements[selected_element].set_deselect()
    if e.keysym == 'Up':
        if selected_element == 0:
            menu_stack.set_state(elements.__len__() - 1)
        else:
            menu_stack.set_state(menu_stack.get_state() - 1)
    elif e.keysym == 'Down':
        if selected_element+1 == elements.__len__():
            menu_stack.set_state(0)
        else:
            menu_stack.set_state(menu_stack.get_state() + 1)
    elif e.keysym == 'space':
        canvas.create_rectangle(0,0,500,500,fill="grey")
        elements[selected_element].do()

    elif e.keysym == "Left":
        menu_stack.pop()

    selected_element = menu_stack.get_state()
    elements = menu_stack.get_menu()
    elements[selected_element].set_select()

selected_element = 0
canvas.bind_all('<Key>', move_select_or_do)
element1.set_select()
while True:
    window.update()
    for i in menu_stack.get_menu():
        i.render()

    elements= menu_stack.get_menu()
    selected_element = menu_stack.get_state()

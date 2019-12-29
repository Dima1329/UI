from tkinter import *
from UIButton import *
from UIElement import UIElement
from UIElementBoundaries import *
from UIInfo import *
from UIMenu import UIMenu

window = Tk()
canvas = Canvas(window, width=500, height=500)
canvas.pack()
bounderies1 = UIElementBoundaries(10, 10, 490, 40)
element1 = UIButton("black", "white", "Hellow Word!", canvas, bounderies1, lambda: print("Done Button"))
element1.render()
bounderies2 = UIElementBoundaries(10, 40, 490, 70)
element2 = UIInfo("black", "white", "Hi!", canvas, bounderies2)
element2.render()
bounderies3 = UIElementBoundaries(10, 70, 490, 100)
element3 = UIMenu("black", "white", "Word, is it you?", canvas, bounderies3)
element3.render()
element4 = UIInfo("black", "white", "F", canvas, bounderies1)
element5 = UIInfo("black", "white", "l", canvas, bounderies2)
element6 = UIInfo("black", "white", "h", canvas, bounderies3)

elements = [element1, element2, element3]
windowelements = [element4, element5, element6]
mainelements = elements

def move_select_or_do(e):
    global selected_element
    global elements
    elements[selected_element].set_deselect()
    if e.keysym == 'Up':
        if selected_element == 0:
            selected_element = elements.__len__() - 1
        else:
            selected_element += -1
    elif e.keysym == 'Down':
        if selected_element+1 == elements.__len__():
            selected_element = 0
        else:
            selected_element += 1
    elif e.keysym == 'space' and elements[selected_element] != element3:
        elements[selected_element].do()

    elif e.keysym == 'space' and selected_element == 2:
        element3.do(windowelements)
        elements = windowelements
        selected_element = 0

    elif e.keysym == "Left":
        for i in mainelements:
            i.render()
        elements = mainelements

    elements[selected_element].set_select()

selected_element = 0
canvas.bind_all('<Key>', move_select_or_do)
element1.set_select()
while True:
    window.update()
    for i in elements:
        i.render()

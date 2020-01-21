
from UIElement import *


class UIMenu(UIElement):
    def __init__(self, col_select, col_deselect, text, c, ui_boundaries, window, stack):
        super().__init__(col_select, col_deselect, text, c, ui_boundaries)
        self.window = window
        self.s= stack
    def do(self):
        for i in self.s.get_menu():
            self.c.delete(i)
        self.s.push(self.window)




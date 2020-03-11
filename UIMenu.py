
from UIElement import *


class UIMenu(UIElement):
    def __init__(self, col_select, col_deselect, text, c,  window, stack, scroller):
        super().__init__(col_select, col_deselect, text, c)
        self.window = window
        self.s = stack
        self.sc = scroller

    def do(self):
        self.s.push(self.window)
        self.sc.update()

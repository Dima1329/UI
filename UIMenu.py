
from UIElement import *


class UIMenu(UIElement):
    def __init__(self, col_select, col_deselect, text, c,  window, stack, updater):
        super().__init__(col_select, col_deselect, text, c)
        self.window = window
        self.s = stack
        self.updater = updater

    def do(self):
        self.s.push(self.window)
        self.updater.update()

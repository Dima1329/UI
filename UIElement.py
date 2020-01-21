from UIGraphicalElement import *


class UIElement(UIGraphicalElement):

    def __init__(self, col_select, col_deselect, text, c, ui_boundaries):
        super().__init__(c, col_select, col_deselect, ui_boundaries, text)
        self.selected = False

    def do(self):
        print("Done!")

    def set_select(self):
        self.selected = True

    def set_deselect(self):
        self.selected = False

    def render(self):
        self.draw_rect(self.selected)
        self.draw_text(self.selected)


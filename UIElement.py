from UIGraphicalElement import *

#a = "l"
#b="l"
#a==b-false a.compare(b)
class UIElement(UIGraphicalElement):
 
    def __init__(self, col_select, col_deselect, text, c):
        super().__init__(c, col_select, col_deselect, text)
        self.selected = False

    def do(self):
        print("No action")

    def set_select(self):
        self.selected = True

    def set_deselect(self):
        self.selected = False

    def render(self):
        self.draw_rect(self.selected)
        self.draw_text(self.selected)

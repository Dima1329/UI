from UIElement import *


class UIButton(UIElement):
    def __init__(self, col_select, col_deselect, text, c, ui_boundaries, do_functor):
        super().__init__(col_select, col_deselect, text, c, ui_boundaries)
        self.do = do_functor

    def do(self):
        self.do()

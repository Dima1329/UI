
class UIGraphicalElement:
    def __init__(self, canvas, col_select, col_deselect, ui_boudaries, text):
        self.col_select = col_select
        self.col_deselect = col_deselect
        self.c = canvas
        self.ui_boundaries = ui_boudaries
        self.id_text = 0
        self.id_rect = 0
        self.text = text

    def draw_rect(self, is_selected):
        if self.id_rect != 0:
            self.c.delete(self.id_rect)
        self.id_rect = self.c.create_rectangle(self.ui_boundaries.x,
                                               self.ui_boundaries.y,
                                               self.ui_boundaries.x1,
                                               self.ui_boundaries.y1,
                                               fill=self.col_select if is_selected else self.col_deselect,
                                               outline="black")

    def draw_text(self, is_selected):
        if self.id_text != 0:
            self.c.delete(self.id_text)
        self.id_text = self.c.create_text(self.ui_boundaries.get_center_x(),
                                          self.ui_boundaries.get_center_y(),
                                          text=self.text,
                                          fill=self.col_deselect if is_selected else self.col_select)

class UIElementBoundaries:
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def get_left_top(self):
        return self.x, self.y

    def get_right_down(self):
        return self.x1, self.y1

    def get_center_x(self):
        return self.x + ((self.x1 - self.x) / 2)

    def get_center_y(self):
        return self.y + ((self.y1 - self.y) / 2)
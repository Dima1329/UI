from UIElementBoundaries import UIElementBoundaries


class UIUpdaterOfBoundaries:
    def __init__(self):
        self.boundaries1 = UIElementBoundaries(10, 10, 490, 40)
        self.boundaries2 = UIElementBoundaries(10, 40, 490, 70)
        self.boundaries3 = UIElementBoundaries(10, 70, 490, 100)
        self.boundaries_out_of_side = UIElementBoundaries(10, 100000000, 490, 1000000000)
        self.stack = None

    def update(self):
        if len(self.stack.stack_windows[-1]) ==1:
            self.stack.stack_windows[-1][0].set_boundaries(self.boundaries1)
        elif len(self.stack.stack_windows[-1]) == 2:
                self.stack.stack_windows[-1][0].set_boundaries(self.boundaries1)
                self.stack.stack_windows[-1][1].set_boundaries(self.boundaries2)
        elif len(self.stack.stack_windows[-1]) < 4:
            self.stack.stack_windows[-1][0].set_boundaries(self.boundaries1)
            self.stack.stack_windows[-1][1].set_boundaries(self.boundaries2)
            self.stack.stack_windows[-1][2].set_boundaries(self.boundaries3)

    def set_stack(self, stack):
        self.stack = stack

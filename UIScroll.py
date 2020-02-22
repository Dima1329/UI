from UIElementBoundaries import UIElementBoundaries


class UIScroller:
    def __init__(self):
        self.boundaries1 = UIElementBoundaries(10, 10, 490, 40)
        self.boundaries2 = UIElementBoundaries(10, 40, 490, 70)
        self.boundaries3 = UIElementBoundaries(10, 70, 490, 100)
        self.boundaries_out_of_side = UIElementBoundaries(10, 100000000, 490, 1000000000)
        self.stack = None

    def set_stack(self, stack):
        self.stack = stack

    def window_up(self):
        if self.stack.get_state() != 0:
            self.stack.set_state(self.stack.get_state() - 1)
        state = self.stack.get_state()
        if len(self.stack.stack_windows[-1]) < 4:
            pass
        elif state == len(self.stack.stack_windows[-1]) - 2:
            self.hide_other_el()
            self.stack.stack_windows[-1][state].set_boundaries(self.boundaries1)
            self.stack.stack_windows[-1][state + 1].set_boundaries(self.boundaries2)
        elif state == len(self.stack.stack_windows[-1]) - 1:
            self.stack.stack_windows[-1][state - 1].set_boundaries(self.boundaries_out_of_side)
            self.stack.stack_windows[-1][state].set_boundaries(self.boundaries1)
        elif state > 2:
            self.hide_other_el()
            self.stack.stack_windows[-1][state + 0].set_boundaries(self.boundaries1)
            self.stack.stack_windows[-1][state + 1].set_boundaries(self.boundaries2)
            self.stack.stack_windows[-1][state + 2].set_boundaries(self.boundaries3)
        elif state < 3:
            self.hide_other_el()
            self.stack.stack_windows[-1][0].set_boundaries(self.boundaries1)
            self.stack.stack_windows[-1][1].set_boundaries(self.boundaries2)
            self.stack.stack_windows[-1][2].set_boundaries(self.boundaries3)

    def window_down(self):
        if self.stack.get_state() + 1 != len(self.stack.get_menu()):
            self.stack.set_state(self.stack.get_state() + 1)
        state = self.stack.get_state()
        if len(self.stack.stack_windows[-1]) < 4:
            pass
        elif state == len(self.stack.stack_windows[-1]) - 2:
            self.hide_other_el()
            self.stack.stack_windows[-1][state].set_boundaries(self.boundaries1)
            self.stack.stack_windows[-1][state + 1].set_boundaries(self.boundaries2)
        elif state == len(self.stack.stack_windows[-1]) - 1:
            self.stack.stack_windows[-1][state - 1].set_boundaries(self.boundaries_out_of_side)
            self.stack.stack_windows[-1][state].set_boundaries(self.boundaries1)
        elif state > 2:
            self.hide_other_el()
            self.stack.stack_windows[-1][state + 0].set_boundaries(self.boundaries1)
            self.stack.stack_windows[-1][state + 1].set_boundaries(self.boundaries2)
            self.stack.stack_windows[-1][state + 2].set_boundaries(self.boundaries3)
        elif state < 3:
            self.hide_other_el()
            self.stack.stack_windows[-1][0].set_boundaries(self.boundaries1)
            self.stack.stack_windows[-1][1].set_boundaries(self.boundaries2)
            self.stack.stack_windows[-1][2].set_boundaries(self.boundaries3)

    def hide_other_el(self):
        state = self.stack.get_state()
        for i in self.stack.stack_windows[-1]:
            if (i != self.stack.stack_windows[-1][state] or i != self.stack.stack_windows[-1][state + 1] or i !=
                    self.stack.stack_windows[-1][state + 2]):
                i.set_boundaries(self.boundaries_out_of_side)

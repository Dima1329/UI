from UIElementBoundaries import UIElementBoundaries


class UIScroller:
    def __init__(self):
        self.boundaries1 = UIElementBoundaries(10, 10, 490, 40)
        self.boundaries2 = UIElementBoundaries(10, 40, 490, 70)
        self.boundaries3 = UIElementBoundaries(10, 70, 490, 100)
        self.boundaries_out_of_side = UIElementBoundaries(10, 100000000, 490, 1000000000)
        self.nwas = None

    def update(self):
        state = self.nwas.get_state()
        if len(self.nwas.get_menu()) < 4:
            pass
        elif state == len(self.nwas.get_menu()) - 2:
            self.hide_out_of_window_elememts()
            self.nwas.get_menu()[state].set_boundaries(self.boundaries1)
            self.nwas.get_menu()[state + 1].set_boundaries(self.boundaries2)
        elif state == len(self.nwas.get_menu()) - 1:
            self.nwas.get_menu()[state - 1].set_boundaries(self.boundaries_out_of_side)
            self.nwas.get_menu()[state].set_boundaries(self.boundaries1)
        elif state > 2:
            self.hide_out_of_window_elememts()
            self.nwas.get_menu()[state + 0].set_boundaries(self.boundaries1)
            self.nwas.get_menu()[state + 1].set_boundaries(self.boundaries2)
            self.nwas.get_menu()[state + 2].set_boundaries(self.boundaries3)
        elif state < 3:
            self.hide_out_of_window_elememts()
            self.nwas.get_menu()[0].set_boundaries(self.boundaries1)
            self.nwas.get_menu()[1].set_boundaries(self.boundaries2)
            self.nwas.get_menu()[2].set_boundaries(self.boundaries3)

    def set_nwas(self, nwas):
        self.nwas = nwas

    def window_up(self):
        if self.nwas.get_state() != 0:
            self.nwas.set_state(self.nwas.get_state() - 1)
            self.update()

    def window_down(self):
        if self.nwas.get_state() + 1 != len(self.nwas.get_menu()):
            self.nwas.set_state(self.nwas.get_state() + 1)
            self.update()

    def hide_out_of_window_elememts(self):
        for i in self.nwas.get_menu():
            if self.is_in_window(i):
                i.set_boundaries(self.boundaries_out_of_side)

    def is_in_window(self, i):
        state = self.nwas.get_state()
        return i != self.nwas.get_menu()[state] or i != self.nwas.get_menu()[state + 1] or i != self.nwas.get_menu()[state + 2]

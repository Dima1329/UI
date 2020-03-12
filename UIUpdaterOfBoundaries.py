from UIElementBoundaries import UIElementBoundaries


class UIUpdaterOfBoundaries:
    def __init__(self):
        self.boundaries1 = UIElementBoundaries(10, 10, 490, 40)
        self.boundaries2 = UIElementBoundaries(10, 40, 490, 70)
        self.boundaries3 = UIElementBoundaries(10, 70, 490, 100)
        self.boundaries_out_of_side = UIElementBoundaries(10, 100000000, 490, 1000000000)
        self.nwas = None

    def update(self):
        if len(self.nwas.get_menu()) ==1:
            self.nwas.get_menu()[-1][0].set_boundaries(self.boundaries1)
        elif len(self.nwas.get_menu()) == 2:
                self.nwas.get_menu()[0].set_boundaries(self.boundaries1)
                self.nwas.get_menu()[1].set_boundaries(self.boundaries2)
        elif len(self.nwas.get_menu()) < 4:
            self.nwas.get_menu()[0].set_boundaries(self.boundaries1)
            self.nwas.get_menu()[1].set_boundaries(self.boundaries2)
            self.nwas.get_menu()[2].set_boundaries(self.boundaries3)

    def set_nwas(self, nwas):
        self.nwas = nwas

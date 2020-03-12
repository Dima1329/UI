class UINowWindowAndState:
    def __init__(self, stack):
        self.stack = stack


    def get_state(self):
        return self.stack.get_state()

    def get_menu(self):
        return self.stack.get_menu()

    def set_state(self, state):
        self.stack.set_state(state)

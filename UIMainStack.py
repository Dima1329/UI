class UIMainStack():
    def __init__(self,scroller):
        self.scroller = scroller
        self.stack_windows = []
        self.stack_state = []

    def pop(self):
        if len(self.stack_windows) > 1:
            self.stack_windows.pop()
            self.stack_state.pop()
            for element in self.get_menu():
                element.show()

    def push(self, n):
        if len(self.stack_windows) > 0:
            for element in self.get_menu():
                element.hide()

        self.stack_windows.append(n)
        self.stack_state.append(0)

    def get_state(self):
        return self.stack_state[-1]

    def set_state(self, state):
        self.stack_state[-1] = state

    def get_menu(self):
        return self.stack_windows[-1]

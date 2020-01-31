from UIGraphicalElement import UIGraphicalElement


class UIMainStack:


    def __init__(self,c):
        self.c = c
        self.stack_windows = []
        self.stack_state = []
        self.is_down = "False"

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


    def set_is_down(self, _is_):
        self.is_down = _is_
    def get_is_down(self):
        return self.is_down
    def get_menu(self):
        if len(self.stack_windows[-1]) == 3:
            return self.stack_windows[-1]

        elif len(self.stack_windows[-1]) > 3 and self.stack_state[-1] < 3 and not self.get_is_down() == "True":
            return [self.stack_windows[-1][0], self.stack_windows[-1][1], self.stack_windows[-1][2]]

        elif len(self.stack_windows[-1]) > 3 and self.stack_state[-1] < 3 and self.get_is_down() == "Up":
            self.set_state(2)
            return [self.stack_windows[-1][0], self.stack_windows[-1][1], self.stack_windows[-1][2]]
        else:
            UIGraphicalElement.hide_everything(self.c)
            self.set_state(0)
            self.set_is_down("True")
            return self.stack_windows[-1][3:]


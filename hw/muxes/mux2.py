class mux2:

    def __init__(self):
        self.selector = hex(00)
        self.input_1 = None
        self.input_2 = None
        self.output = None

    """ Selector """

    def get_selector(self):
        return self.selector

    def set_selector(self, value):
        self.selector = value
        if self.selector == hex(1) or self.selector == "1":
            self.set_output(self.input_2)
        else:
            self.set_output(self.input_1)

    def del_selector(self):
        del self.selector

    selector = property(get_selector, set_selector, del_selector, 'Selector')

    """ Input 1 """

    def get_input_1(self):
        return self.input_1

    def set_input_1(self, value):
        self.input_1 = value

    def del_input_1(self):
        del self.input_1

    input_1 = property(get_input_1, set_input_1, del_input_1, 'Input 1')

    """ Input 2 """

    def get_input_2(self):
        return self.input_2

    def set_input_2(self, value):
        self.input_2 = value

    def del_input_2(self):
        del self.input_2

    input_2 = property(get_input_2, set_input_2, del_input_2, 'Input 2')

    """ Output """

    def get_output(self):
        return self.output

    def set_output(self, value):
        self.output = value

    def del_output(self):
        del self.output

    output = property(get_output, set_output, del_output, 'Output')

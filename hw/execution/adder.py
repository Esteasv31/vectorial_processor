class adder:

    def __init__(self):
        self.operand_1 = hex(0)
        self.operand_2 = hex(4)
        self.output = self.add()

    """ Operand 1 """

    def get_operand_1(self):
        return self.operand_1

    def set_operand_1(self, value):
        self.operand_1 = value

    def del_operand_1(self):
        del self.operand_1

    operand_1 = property(get_operand_1, set_operand_1, del_operand_1, 'Operand 1')

    """ Operand 2 """

    def get_operand_2(self):
        return self.operand_2

    def set_operand_2(self, value):
        self.operand_2 = value

    def del_operand_2(self):
        del self.operand_2

    operand_2 = property(get_operand_2, set_operand_2, del_operand_2, 'Operand 2')

    """ Output """

    def get_output(self):
        return self.output

    def set_output(self, value):
        self.output = value

    def del_output(self):
        del self.output

    output = property(get_output, set_output, del_output, 'Output')

    """ Function """

    def add(self):
        return hex(int(self.operand_1, 16) + int(self.operand_2, 16))

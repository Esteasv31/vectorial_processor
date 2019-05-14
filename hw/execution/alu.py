""" Control Signals

    signals = {
        "0000": add,
        "0001": sub,
        "0010": mul,
        "0011": div,
        "0100": shiftl,
        "0101": shiftr,
        "0110": xor,
        "0111": pow_,
        "1000": sqrt,
        "1001": cshiftl,
        "1010": cshiftr
    }
"""


class ALU:

    def __init__(self):
        self.control = hex(0)
        self.input_1 = None
        self.input_2 = None
        self.result = None
        self.int_bits = 8

    """ Control """

    def get_control(self):
        return self.control

    def set_control(self, value):
        self.control = value
        if self.control == "0000":
            self.result = self.add()
        elif self.control == "0001":
            self.result = self.sub()
        elif self.control == "0010":
            self.result = self.mul()
        elif self.control == "0011":
            self.result = self.div()
        elif self.control == "0100":
            self.result = self.shiftl()
        elif self.control == "0101":
            self.result = self.shiftr()
        elif self.control == "0110":
            self.result = self.xor()
        elif self.control == "0111":
            self.result = self.pow_()
        elif self.control == "1000":
            self.result = self.sqrt()
        elif self.control == "1001":
            self.result = self.cshiftl()
        elif self.control == "1010":
            self.result = self.cshiftr()
        else:
            self.result = "XXXXXXXX"

    def del_control(self):
        del self.control

    control = property(get_control, set_control, del_control, 'Control')

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

    """ Result """

    def get_result(self):
        self.control = self.set_control(self.control)
        return self.result

    def set_result(self, value):
        self.result = value

    def del_result(self):
        del self.result

    result = property(get_result, set_result, del_result, 'Result')

    """ ADD """

    def add(self):
        return self.input_1 + self.input_2

    """ SUB """

    def sub(self):
        return self.input_1 - self.input_2

    """ MUL """

    def mul(self):
        return self.input_1 * self.input_2

    """ DIV """

    def div(self):
        return self.input_1 / self.input_2

    """ SHIFT L """

    def shiftl(self):
        return self.input_1 << self.input_2

    """ SHIFT R """

    def shiftr(self):
        return self.input_1 >> self.input_2

    """ XOR """

    def xor(self):
        return self.input_1 ^ self.input_2

    """ POW """

    def pow_(self):
        return self.input_1 ** self.input_2

    """ SQRT """

    def sqrt(self):
        return int(self.input_1 ** (1 / self.input_2))

    """ C SHIFT L """

    def cshiftl(self):
        binary = "{0:b}".format(self.input_1)
        return binary[self.input_2:len(binary)] + binary[0:self.input_2]

    """ C SHIFT R """

    def cshiftr(self):
        binary = "{0:b}".format(self.input_1)
        return binary[-self.input_2:len(binary)] + binary[0:-self.input_2]

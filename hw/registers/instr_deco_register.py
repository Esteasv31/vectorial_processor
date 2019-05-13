class instr_deco_register:

    def __init__(self):
        self._clk = 0
        self._reset = 1
        self._in_pointer = hex(0)
        self._out_pointer = hex(0)

    """ CLK define """

    def get_clk(self):
        return self._clk

    def set_clk(self, value):
        self._clk = value
        if self._clk == 1:
            self.set_out_pointer(self.get_in_pointer)

    def del_clk(self):
        del self._clk

    clk = property(get_clk, set_clk, del_clk, 'CLK property')

    """ RESET define """

    def get_reset(self):
        return self._reset

    def set_reset(self, value):
        self._reset = value
        if self._reset == 0:
            self._in_pointer = 0
            self._out_pointer = 0

    def del_reset(self):
        del self._reset

    reset = property(get_reset, set_reset, del_reset, 'RESET property')

    """ IN_POINTER define """

    def get_in_pointer(self):
        return self._in_pointer

    def set_in_pointer(self, value):
        self._in_pointer = value

    def del_in_pointer(self):
        del self._in_pointer

    in_pointer = property(get_in_pointer, set_in_pointer, del_in_pointer, 'IN POINTER property')

    """ OUT_POINTER define """

    def get_out_pointer(self):
        return self._out_pointer

    def set_out_pointer(self, value):
        self._out_pointer = value

    def del_out_pointer(self):
        del self._out_pointer

    out_pointer = property(get_out_pointer, set_out_pointer, del_out_pointer, 'OUT POINTER property')

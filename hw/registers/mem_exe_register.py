class mem_exe_reg:

    def __init__(self):
        """ Inputs """
        self.in_vec_reg_1 = None
        self.in_vec_reg_2 = None
        self.in_scalar = None
        self.in_imm = None

        """ Outputs """
        self.out_vec_reg_1 = None
        self.out_vec_reg_2 = None
        self.out_scalar = None
        self.out_imm = None

    """ Inputs """

    """ Vec Reg 1 """

    def get_in_vec_reg_1(self):
        return self.in_vec_reg_1

    def set_in_vec_reg_1(self, value):
        self.in_vec_reg_1 = value

    def del_in_vec_reg_1(self):
        del self.in_vec_reg_1

    in_vec_reg_1 = property(get_in_vec_reg_1, set_in_vec_reg_1, del_in_vec_reg_1, 'In Vec Reg 1')

    """ Vec Reg 2 """

    def get_in_vec_reg_2(self):
        return self.in_vec_reg_2

    def set_in_vec_reg_2(self, value):
        self.in_vec_reg_2 = value

    def del_in_vec_reg_2(self):
        del self.in_vec_reg_2

    in_vec_reg_2 = property(get_in_vec_reg_2, set_in_vec_reg_2, del_in_vec_reg_2, 'In Vec Reg 2')

    """ Scalar """

    def get_in_scalar(self):
        return self.in_scalar

    def set_in_scalar(self, value):
        self.in_scalar = value

    def del_in_scalar(self):
        del self.in_scalar

    in_scalar = property(get_in_scalar, set_in_scalar, del_in_scalar, 'In Scalar')

    """ IMM """

    def get_in_imm(self):
        return self.in_imm

    def set_in_imm(self, value):
        self.in_imm = value

    def del_in_imm(self):
        del self.in_imm

    in_imm = property(get_in_imm, set_in_imm, del_in_imm, 'In Imm')

    """ Outputs """

    """ Vec Reg 1 """

    def get_out_vec_reg_1(self):
        return self.out_vec_reg_1

    def set_out_vec_reg_1(self, value):
        self.out_vec_reg_1 = value

    def del_out_vec_reg_1(self):
        del self.out_vec_reg_1

    out_vec_1 = property(get_out_vec_reg_1, set_out_vec_reg_1, del_out_vec_reg_1, 'Out Vec Reg 1')

    """ Vec Reg 2 """

    def get_out_vec_reg_2(self):
        return self.out_vec_reg_2

    def set_out_vec_reg_2(self, value):
        self.out_vec_reg_2 = value

    def del_out_vec_reg_2(self):
        del self.out_vec_reg_2

    out_vec_reg_2 = property(get_out_vec_reg_2, set_out_vec_reg_2, del_out_vec_reg_2, 'Out Vec Reg 2')

    """ Scalar """

    def get_out_scalar(self):
        return self.out_scalar

    def set_out_scalar(self, value):
        self.out_scalar = value

    def del_out_scalar(self):
        del self.out_scalar

    out_scalar = property(get_out_scalar, set_out_scalar, del_out_scalar, 'Out Scalar')

    """ Imm """

    def get_out_imm(self):
        return self.out_imm

    def set_out_imm(self, value):
        self.out_imm = value

    def del_out_imm(self):
        del self.out_imm

    out_imm = property(get_out_imm, set_out_imm, del_out_imm, 'Out Imm ')
